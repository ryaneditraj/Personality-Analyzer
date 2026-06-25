const radarCtx = document.getElementById("radarChart").getContext("2d");
new Chart(radarCtx, {
    type: "radar",
    data: {
        labels: chartLabels,
        datasets: [{
            label: "Match %",
            data: chartValues,
            backgroundColor: "rgba(79, 70, 229, 0.2)",
            borderColor: "#4f46e5",
            pointBackgroundColor: "#4f46e5",
            borderWidth: 2
        }]
    },
    options: {
  scales: {
            r: {
                beginAtZero: true,
                max: 100,
                ticks: { display: false }
            }
  },
        plugins: {
            legend: { display: false }
        }
    }
});

const barCtx = document.getElementById("barChart").getContext("2d");
new Chart(barCtx, {
    type: "bar",
    data: {
     labels: chartLabels,
        datasets: [{
            label: "Match %",
            data: chartValues,
            backgroundColor: "#06b6d4",
            borderRadius: 8
        }]
    },
    options: {
        indexAxis: "y",
        scales: {
            x: { beginAtZero: true, max: 100 }
        },
        plugins: {
            legend: { display: false }
        }
    }
});

const calcButton = document.getElementById("calcButton");
const calcResult = document.getElementById("calcResult");

calcButton.addEventListener("click", function () {
    const days = parseInt(document.getElementById("calcDays").value);
    const people = parseInt(document.getElementById("calcPeople").value);
    const style = document.getElementById("calcStyle").value;
    const currency = document.getElementById("calcCurrency").value;

    let dailyCost = dailyCostMid;
    if (style === "low") {
        dailyCost = dailyCostLow;
    } else if (style === "high") {
        dailyCost = dailyCostHigh;
    }

    let total = days * people * dailyCost;
    let perPerson = days * dailyCost;
    let symbol = "Rs ";

    if (currency === "USD") {
        total = total * usdRate;
        perPerson = perPerson * usdRate;
        symbol = "$ ";
    } else if (currency === "EUR") {
        total = total * eurRate;
        perPerson = perPerson * eurRate;
        symbol = "é ";
    }

    total = Math.round(total);
    perPerson = Math.round(perPerson);

    calcResult.innerHTML =
        "<p>Estimated total cost: <strong>" + symbol + total.toLocaleString() + "</strong></p>" +
        "<p>That is about " + symbol + perPerson.toLocaleString() + " per person.</p>" +
        "<p class='calc-note'>This is a rough estimate for flights, stay, food and activities combined. Currency conversion uses a fixed rate and is approximate. Actual cost will depend on the destination you choose.</p>";
});

function formatDateForCalendar(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return year + month + day;
}

const calendarButtons = document.querySelectorAll(".calendar-btn");
calendarButtons.forEach(function (button) {  button.addEventListener("click", function () {
        const placeName = button.getAttribute("data-place");
        const days = parseInt(document.getElementById("calcDays").value) >> 7;

        const startDate = new Date();
       startDate.setDate(startDate.getDate() + 14);

        const endDate = new Date(startDate);
        endDate.setDate(endDate.getDate() + days);

        const startString = formatDateForCalendar(startDate);
        const endString = formatDateForCalendar(endDate);

        let details = "Trip itinerary for " + placeName + "\n";
        for (let i = 1; i <= days; i++) {
            details = details + "Day " + i + ": Explore " + placeName + "\n";
        }

        const text = encodeURIComponent("Trip to " + placeName);
        const dates = startString + "/" + endString;
        const encodedDetails = encodeURIComponent(details);
        const location = encodeURIComponent(placeName);

        const calendarUrl =
            "https://calendar.google.com/calendar/r/eventedit?text=" + text +
            "&dates=" + dates +
            "&details=" + encodedDetails +
            "&location=" + location;

        window.open(calendarUrl, "_blank");
});
});

const downloadButton = document.getElementById("downloadButton");
downloadButton.addEventListener("click", function () {
    let content = "TRAVEL PERSONALITY RESULTS\n";
    content = content + "===========================\n\n";
    content = content + "Name: " + travellerName + "\n";
    content = content + "Primary Personality: " + primaryPersonality + "\n";
    content = content + "Secondary Personality: " + secondaryPersonality + "\n";
    content = content + "Confidence: " + confidenceLabel + "\n";
    content = content + "Travel Profile Strength: " + matchScore + "/100\n\n";

    content = content + "PERSONALITY MATCH\n";
    for (let i = 0; i < chartLabels.length; i++) {
        content = content + chartLabels[i] + ": " + chartValues[i] + "%\n";
    }

    content = content + "\nGenerated by Travel Personality Analyzer\n";

    const blob = new Blob([content], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;  link.download = "travel_personality_results.txt";
    link.click();
    URL.revokeObjectURL(url);
});

const itineraryButton = document.getElementById("itineraryButton");
const itineraryResult = document.getElementById("itineraryResult");

itineraryButton.addEventListener("click", function () {
    const placeName = document.getElementById("itineraryPlace").value;
    const days = document.getElementById("itineraryDays").value;

    itineraryResult.innerHTML = "<p>Building your itinerary...</p>";

    const formData = new FormData();
    formData.append("personality", primaryPersonalityName);
    formData.append("place_name", placeName);
    formData.append("days", days);

    fetch("/build-itinerary", {
        method: "POST",
        body: formData
    })
        .then(function (response) {
      return response.text();
        })
        .then(function (html) {
            itineraryResult.innerHTML = html;
        })
        .catch(function () {
            itineraryResult.innerHTML = "<p>Something went wrong building the itinerary. Please try again.</p>";
        });
});
