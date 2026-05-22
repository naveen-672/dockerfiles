const express = require("express");

const app = express();

app.set("view engine", "ejs");

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));

const hotels = [
  {
    name: "Luxury Hotel",
    place: "Goa",
    price: 5000
  },
  {
    name: "Sea View Resort",
    place: "Mumbai",
    price: 7000
  },
  {
    name: "Mountain Stay",
    place: "Manali",
    price: 4000
  }
];

app.get("/", (req, res) => {

  res.render("index", {
    hotels: hotels,
    success: false
  });

});

app.post("/book", (req, res) => {

  res.render("index", {
    hotels: hotels,
    success: true
  });

});

app.listen(3000, "0.0.0.0", () => {
  console.log("Server running on port 3000");
});
