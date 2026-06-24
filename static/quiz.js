const steps = document.querySelectorAll(".step");
const totalSteps = steps.length - 1;
let currentStep = 0;

const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const submitBtn = document.getElementById("submitBtn");
const progressFill = document.getElementById("progressFill");
const progressLabel = document.getElementById("progressLabel");

function updateProgress() {
    const percent = (currentStep / totalSteps) * 100;
    progressFill.style.width = percent + "%";
    progressLabel.textContent = "Question " + (currentStep + 1) + " of " + (totalSteps + 1);
}

function showStep(index) {
   steps.forEach(function (step) {
        step.classList.remove("active");
   });
    steps[index].classList.add("active");

    if (index === 0) {
        prevBtn.style.display = "none";
    } else {
        prevBtn.style.display = "inline-block";
    }

    if (index === totalSteps) {
        nextBtn.style.display = "none";
        submitBtn.style.display = "inline-block";
    } else {
        nextBtn.style.display = "inline-block";
        submitBtn.style.display = "none";
    }

    updateProgress();
}

function currentStepIsValid() {
    const activeStep = steps[currentStep];
    const inputs = activeStep.querySelectorAll("input");

    if (inputs.length === 0) {
        return true;
    }

    if (inputs[0].type === "text") {
        return inputs[0].value.trim().length > 0;
    }

    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            return true;
        }
    }
    return false;
}

nextBtn.addEventListener("click", function () {
    if (!currentStepIsValid()) {
        alert("Please answer before moving on.");
        return;
    }
    if (currentStep < totalSteps) {
        currentStep = currentStep + 1;
        showStep(currentStep);
    }
});

prevBtn.addEventListener("click", function () {
    if (currentStep > 0) {
        currentStep = currentStep - 1;
        showStep(currentStep);
    }
});

const allOptionCards = document.querySelectorAll(".option-card");
allOptionCards.forEach(function (card) {
    card.addEventListener("click", function () {
        const radioName = card.querySelector("input").name;
        const sameNameInputs = document.querySelectorAll('input[name="' + radioName + '"]');
        sameNameInputs.forEach(function (input) {
          input.closest(".option-card").classList.remove("selected");
        });
        card.classList.add("selected");
    });
});

showStep(currentStep);