from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    error = ""

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hesap Makinesi</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }
            .calculator-container {
                background-color: white;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                padding: 30px;
                width: 100%;
                max-width: 400px;
                margin-top: 20px;
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            input, select {
                width: 100%;
                padding: 12px;
                margin-bottom: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
            }
            input:focus, select:focus {
                outline: none;
                border-color: #3498db;
                box-shadow: 0 0 5px rgba(52, 152, 219, 0.5);
            }
            button {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 12px 20px;
                width: 100%;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            button:hover {
                background-color: #2980b9;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 5px;
                background-color: #e8f4fc;
                color: #2c3e50;
                text-align: center;
                font-size: 18px;
            }
            .error {
                margin-top: 20px;
                padding: 15px;
                border-radius: 5px;
                background-color: #fde8e8;
                color: #e74c3c;
                text-align: center;
                font-size: 16px;
            }
            .footer {
                margin-top: 30px;
                text-align: center;
                color: #7f8c8d;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="calculator-container">
            <h1> Hesap Makinesi</h1>
            <form method="post">
                <div class="form-group">
                    <input type="text" name="num1" placeholder="Birinci sayı" required>
                </div>
                <div class="form-group">
                    <input type="text" name="num2" placeholder="İkinci sayı" required>
                </div>
                <div class="form-group">
                    <select name="operation">
                        <option value="add">Toplama</option>
                        <option value="subtract">Çıkarma</option>
                        <option value="multiply">Çarpma</option>
                        <option value="divide">Bölme</option>
                    </select>
                </div>
                <button type="submit">Hesapla</button>
            </form>
    """

    if request.method == "POST":
        try:
            num1 = request.form.get("num1", "").strip()
            num2 = request.form.get("num2", "").strip()
            operation = request.form.get("operation", "")

            if not num1 or not num2:
                raise ValueError("Boş giriş")

            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = f"{num1} + {num2} = {num1 + num2}"
            elif operation == "subtract":
                result = f"{num1} - {num2} = {num1 - num2}"
            elif operation == "multiply":
                result = f"{num1} × {num2} = {num1 * num2}"
            elif operation == "divide":
                if num2 == 0:
                    error = "Sıfıra bölünemez!"
                else:
                    result = f"{num1} ÷ {num2} = {num1 / num2}"
            else:
                error = "Geçersiz işlem!"
        except ValueError:
            error = "Lütfen geçerli bir sayı girin."

    if result != "":
        html += f"<div class='result'>{result}</div>"
    if error:
        html += f"<div class='error'>{error}</div>"

    html += """
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
