import ollama
import re
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# ---------------------------
# DATABASE CONNECTION
# ---------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mall_db"
)

cursor = db.cursor(dictionary=True)


# =========================================
# LLM FUNCTION
# =========================================
def generate_sql_query(user_input):

    prompt = f"""
You are an expert MySQL query generator.

IMPORTANT RULES:
- Return ONLY the SQL query.
- Do NOT include markdown.
- Query must start with SELECT.
- Do NOT generate DELETE, DROP, UPDATE, INSERT.

Database Schema:

categories(category_id, category_name)
products(product_id, product_name, category_id, price, stock)
customers(customer_id, customer_name, city)
sales(sale_id, product_id, customer_id, quantity, sale_date)

Query:
{user_input}
"""

    try:
        response = ollama.chat(
            model="phi:latest",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        sql_query = response["message"]["content"]

        # 🔍 DEBUG (important)
        print("\nRAW LLM OUTPUT:\n", sql_query)

        # ----------------------------
        # CLEAN MARKDOWN
        # ----------------------------
        sql_query = re.sub(r"```sql", "", sql_query, flags=re.IGNORECASE)
        sql_query = sql_query.replace("```", "").strip()

        # Remove extra spaces/newlines
        sql_query = " ".join(sql_query.split())

        # ----------------------------
        # EXTRACT SELECT (semicolon optional)
        # ----------------------------
        match = re.search(r"(SELECT .*?)(;|$)", sql_query, re.IGNORECASE)

        if match:
            sql_query = match.group(1).strip()
        else:
            return None

        # ----------------------------
        # SAFETY CHECK
        # ----------------------------
        if "select" not in sql_query.lower():
            return None

        forbidden = ["delete", "drop", "update", "insert", "alter", "truncate"]

        for word in forbidden:
            if word in sql_query.lower():
                return None

        print("CLEAN SQL:", sql_query)

        return sql_query

    except Exception as e:
        print("LLM Error:", e)
        return None


# =========================================
# ROUTE
# =========================================
@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    sql_query = None
    error = None

    if request.method == "POST":
        user_query = request.form.get("query")

        sql_query = generate_sql_query(user_query)

        if sql_query:
            try:
                cursor.execute(sql_query)
                results = cursor.fetchall()
            except Exception as e:
                error = f"Database Error: {e}"
        else:
            error = "Invalid or unsafe query generated."

    return render_template(
        "index.html",
        results=results,
        sql_query=sql_query,
        error=error
    )


# =========================================
# RUN APP
# =========================================
if __name__ == "__main__":
    app.run(debug=True)