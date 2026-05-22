from flask import Flask, render_template_string, request

app = Flask(__name__)

foods = [
    {
        "name": "Burger",
        "price": 199,
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Pizza",
        "price": 299,
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "Pasta",
        "price": 249,
        "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "name": "French Fries",
        "price": 149,
        "image": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?q=80&w=1000&auto=format&fit=crop"
    }
]

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Delivery App</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, Helvetica, sans-serif;
        }

        body{
            background:#0f172a;
            color:white;
        }

        header{
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding:20px 60px;
            background:#111827;
            position:sticky;
            top:0;
            z-index:100;
        }

        .logo{
            font-size:32px;
            font-weight:bold;
            color:#f97316;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin-left:25px;
            transition:0.3s;
        }

        nav a:hover{
            color:#f97316;
        }

        .hero{
            height:85vh;
            background:
            linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.7)),
            url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1400&auto=format&fit=crop');

            background-size:cover;
            background-position:center;

            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            padding:20px;
        }

        .hero-content h1{
            font-size:70px;
            margin-bottom:20px;
        }

        .hero-content span{
            color:#f97316;
        }

        .hero-content p{
            font-size:20px;
            color:#e2e8f0;
            margin-bottom:30px;
        }

        .hero-content button{
            padding:15px 35px;
            border:none;
            background:#f97316;
            color:white;
            border-radius:10px;
            font-size:18px;
            cursor:pointer;
            transition:0.3s;
        }

        .hero-content button:hover{
            background:#ea580c;
            transform:scale(1.05);
        }

        .foods{
            padding:80px 60px;
        }

        .section-title{
            text-align:center;
            font-size:45px;
            margin-bottom:50px;
            color:#f97316;
        }

        .food-container{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
            gap:30px;
        }

        .food-card{
            background:#1e293b;
            border-radius:20px;
            overflow:hidden;
            transition:0.4s;
            box-shadow:0 10px 20px rgba(0,0,0,0.3);
        }

        .food-card:hover{
            transform:translateY(-10px);
        }

        .food-card img{
            width:100%;
            height:250px;
            object-fit:cover;
        }

        .food-info{
            padding:20px;
        }

        .food-info h3{
            font-size:28px;
            margin-bottom:10px;
        }

        .food-info p{
            color:#cbd5e1;
            margin-bottom:15px;
        }

        .price{
            color:#f97316;
            font-size:24px;
            font-weight:bold;
            margin-bottom:15px;
        }

        .food-info button{
            width:100%;
            padding:14px;
            border:none;
            background:#f97316;
            color:white;
            border-radius:10px;
            cursor:pointer;
            font-size:16px;
            transition:0.3s;
        }

        .food-info button:hover{
            background:#ea580c;
        }

        .order-section{
            background:#111827;
            padding:80px 20px;
        }

        .order-box{
            max-width:600px;
            margin:auto;
            background:#1e293b;
            padding:40px;
            border-radius:20px;
        }

        .order-box h2{
            text-align:center;
            margin-bottom:30px;
            color:#f97316;
            font-size:40px;
        }

        .input-group{
            margin-bottom:20px;
        }

        .input-group label{
            display:block;
            margin-bottom:8px;
        }

        .input-group input,
        .input-group select{
            width:100%;
            padding:14px;
            border:none;
            border-radius:10px;
            background:#0f172a;
            color:white;
            outline:none;
        }

        .order-btn{
            width:100%;
            padding:15px;
            border:none;
            background:linear-gradient(to right,#f97316,#fb923c);
            color:white;
            border-radius:10px;
            font-size:18px;
            cursor:pointer;
        }

        footer{
            text-align:center;
            padding:25px;
            background:#020617;
            color:#cbd5e1;
        }

        .success{
            background:#16a34a;
            padding:15px;
            border-radius:10px;
            margin-bottom:20px;
            text-align:center;
        }

        @media(max-width:768px){

            header{
                flex-direction:column;
                gap:15px;
                padding:20px;
            }

            .hero-content h1{
                font-size:45px;
            }

            .foods{
                padding:50px 20px;
            }

        }

    </style>

</head>

<body>

    <header>

        <div class="logo">Foodie</div>

        <nav>
            <a href="#">Home</a>
            <a href="#">Menu</a>
            <a href="#">Orders</a>
            <a href="#">Contact</a>
        </nav>

    </header>

    <section class="hero">

        <div class="hero-content">

            <h1>Delicious Food <span>Delivered Fast</span></h1>

            <p>
                Order your favorite meals online with amazing offers
                and lightning fast delivery.
            </p>

            <button onclick="scrollToMenu()">
                Order Now
            </button>

        </div>

    </section>

    <section class="foods" id="menu">

        <h2 class="section-title">Popular Foods</h2>

        <div class="food-container">

            {% for food in foods %}

            <div class="food-card">

                <img src="{{ food.image }}">

                <div class="food-info">

                    <h3>{{ food.name }}</h3>

                    <p>
                        Fresh and delicious {{ food.name }} prepared with premium ingredients.
                    </p>

                    <div class="price">₹{{ food.price }}</div>

                    <button onclick="selectFood('{{ food.name }}')">
                        Add To Cart
                    </button>

                </div>

            </div>

            {% endfor %}

        </div>

    </section>

    <section class="order-section">

        <div class="order-box">

            <h2>Place Order</h2>

            {% if success %}

            <div class="success">
                🎉 Order placed successfully!
            </div>

            {% endif %}

            <form method="POST">

                <div class="input-group">
                    <label>Food Item</label>
                    <input type="text" name="food" id="foodInput" required>
                </div>

                <div class="input-group">
                    <label>Your Name</label>
                    <input type="text" name="name" required>
                </div>

                <div class="input-group">
                    <label>Address</label>
                    <input type="text" name="address" required>
                </div>

                <div class="input-group">
                    <label>Quantity</label>

                    <select name="quantity">

                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>

                    </select>
                </div>

                <button class="order-btn">
                    Confirm Order
                </button>

            </form>

        </div>

    </section>

    <footer>
        © 2026 Foodie | Food Delivery App
    </footer>

    <script>

        function scrollToMenu(){

            document.getElementById("menu").scrollIntoView({
                behavior:'smooth'
            });

        }

        function selectFood(food){

            document.getElementById("foodInput").value = food;

            window.scrollTo({
                top:document.querySelector(".order-section").offsetTop,
                behavior:'smooth'
            });

        }

    </script>

</body>

</html>

"""

@app.route("/", methods=["GET", "POST"])
def home():

    success = False

    if request.method == "POST":
        success = True

    return render_template_string(
        HTML,
        foods=foods,
        success=success
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
