function calculatePremium(){

let name = document.getElementById("name").value;
let hours = document.getElementById("hours").value;
let risk = document.getElementById("risk").value;
let claims = document.getElementById("claims").value;
let weather = document.getElementById("weather").value;

// Basic validation
if(name === "" || hours === "" || risk === "" || claims === ""){
    alert("Please fill all fields");
    return;
}

fetch("http://127.0.0.1:5000/calculate", {

method: "POST",

headers: {
"Content-Type": "application/json"
},

body: JSON.stringify({
name: name,
hours: hours,
risk: risk,
claims: claims,
weather: weather
})

})

.then(res => res.json())

.then(data => {

// Show result
document.getElementById("result").innerHTML =
"Risk Level: " + risk + " | Weekly Premium: ₹" + data.premium;


// Save history for dashboard
let history = JSON.parse(localStorage.getItem("history")) || [];

history.push({
name: name,
premium: data.premium,
fraud: data.fraud || "No"
});

localStorage.setItem("history", JSON.stringify(history));

})

.catch(error => {
console.log("Error:", error);
alert("Server not running");
});

}


// Dashboard button function
function goDashboard(){
window.location.href = "dashboard.html";
}