
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# Create a new Flask application

main_images = {
    "Compacte auto": "bmw-front.jpg",
    "Luxe sedan": "audi-front.jpg",
    "Ruime SUV": "mercedes-front.jpg"
}


@app.route("/car/<car_name>")
# Show the details of the selected car
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

    return render_template(
        "car_details.html",
        car_name=car_name,
        price=50,
        car_images=car_images
    )


@app.route("/")
# Open the homepage
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
# Open the login page and handle the form
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # Redirect to the homepage if both fields are filled in
        if email and password:
            return redirect("/")

        # Show an error if a field is empty
        return render_template(
            "login.html",
            error_message="Please fill in your email and password."
        )

    return render_template("login.html")


@app.route("/book", methods=["GET", "POST"])
# Handle the booking form
def book():
    if request.method == "POST":
        # Get the information from the booking form
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        selected_car = request.form.get("car", "Compacte auto")
        start_date = request.form.get("start_date", "")
        end_date = request.form.get("end_date", "")

        # Check if all required fields are filled in
        if not name or not email or not start_date or not end_date:
            return render_template(
                "book.html",
                selected_car=selected_car,
                car_image=main_images.get(selected_car, "bmw-front.jpg"),
                error_message="Vul alle velden in."
            )

        # Check if the return date is after the pickup date
        if end_date <= start_date:
            return render_template(
                "book.html",
                selected_car=selected_car,
                car_image=main_images.get(selected_car, "bmw-front.jpg"),
                error_message="De inleverdatum moet na de ophaaldatum liggen."
            )

        # Show the booking confirmation
        return render_template(
            "confirmation.html",
            name=name,
            selected_car=selected_car,
            start_date=start_date,
            end_date=end_date
        )

    # Get the selected car from the URL
    selected_car = request.args.get("car", "Compacte auto")

    return render_template(
        "book.html",
        selected_car=selected_car,
        car_image=main_images.get(selected_car, "bmw-front.jpg")
    )


if __name__ == "__main__":
    # Run the website in debug mode
    app.run(debug=True)
