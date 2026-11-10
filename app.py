
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/car/<car_name>") # open home page
def car_details(car_name):
    image_sets = { 
        
        "Compacte auto": [
            "bmw-front.jpg",
            "bmw-rear.jpg",
            "bmw-side.jpg"
        ],
        "Luxe sedan": [
            "audi-front.jpg",
            "audi-rear.jpg"
        ],
        "Ruime SUV": [
            "mercedes-front.jpg",
            "mercedes-rear.jpg",
            "mercedes-side.jpg"
        ]
    }

    car_images = image_sets.get(car_name, [])

    return render_template( # send the car information to the HTML page
        "car_details.html",
        car_name=car_name,
        price=50,
        car_images=car_images
    )
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["GET", "POST"]) 
# This route handles the booking form
def book():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        selected_car = request.form.get("car", "Compacte auto")
        start_date = request.form.get("start_date", "")
        end_date = request.form.get("end_date", "")

        if not name or not email or not start_date or not end_date:
            return render_template(
                "book.html",
                selected_car=selected_car
            )

        if end_date <= start_date:
            return render_template(
                "book.html",
                selected_car=selected_car,
                error_message="De inleverdatum moet na de ophaaldatum liggen."
            )

        return render_template(
            "confirmation.html",
            name=name,
            selected_car=selected_car,
            start_date=start_date,
            end_date=end_date
        )

    selected_car = request.args.get("car", "Compacte auto")
    return render_template("book.html", selected_car=selected_car)


if __name__ == "__main__":
    app.run(debug=True)
    # Run the website in debug mode