{% if "subject_run_config" in modules %}
<div class="module">
    <h3>Subject Run Config</h3>

    <!-- Frequency Selection -->
    <label>Frequency <span class="required">*</span></label>
    <div class="radio-group">
        <label><input type="radio" name="frequency" value="Daily" onclick="toggleRunConfigInputs()"> Daily</label>
        <label><input type="radio" name="frequency" value="Weekly" onclick="toggleRunConfigInputs()"> Weekly</label>
        <label><input type="radio" name="frequency" value="Monthly_Calendar" onclick="toggleRunConfigInputs()"> Monthly Calendar Days</label>
        <label><input type="radio" name="frequency" value="Monthly_Business" onclick="toggleRunConfigInputs()"> Monthly Business Days</label>
    </div>

    <!-- Conditional Input for Weekly Frequency -->
    <div id="weekly_day_number_container" style="display: none;">
        <label>Weekly Day Number (1-7) <span class="required">*</span></label>
        <input type="number" id="weekly_day_number" class="full-width" min="1" max="7">
    </div>

    <!-- Conditional Input for Monthly Frequencies -->
    <div id="monthly_day_number_container" style="display: none;">
        <label>Day Number (1-31) <span class="required">*</span></label>
        <input type="number" id="monthly_day_number" class="full-width" min="1" max="31">
    </div>
</div>
{% endif %}


function toggleRunConfigInputs() {
    let selectedFrequency = document.querySelector("input[name='frequency']:checked").value;

    let weeklyContainer = document.getElementById("weekly_day_number_container");
    let monthlyContainer = document.getElementById("monthly_day_number_container");

    if (selectedFrequency === "Weekly") {
        weeklyContainer.style.display = "block";
        monthlyContainer.style.display = "none";
    } else if (selectedFrequency === "Monthly_Calendar" || selectedFrequency === "Monthly_Business") {
        weeklyContainer.style.display = "none";
        monthlyContainer.style.display = "block";
    } else {
        weeklyContainer.style.display = "none";
        monthlyContainer.style.display = "none";
    }
}

subject_run_config: {
    frequency: document.querySelector("input[name='frequency']:checked").value,
    weekly_day_number: document.getElementById("weekly_day_number")?.value || null,
    monthly_day_number: document.getElementById("monthly_day_number")?.value || null
}


# Subject Run Config
if "subject_run_config" in data:
    print("\n Subject Run Config:")
    config = data["subject_run_config"]
    print(f"  Frequency: {config['frequency']}")

    # Handle Weekly Day Number (only if Weekly is selected)
    if config["frequency"] == "Weekly":
        print(f"  Weekly Day Number: {config['weekly_day_number']}")

    # Handle Monthly Day Number (only if Monthly Calendar/Business Days is selected)
    if config["frequency"] in ["Monthly_Calendar", "Monthly_Business"]:
        print(f"  Monthly Day Number: {config['monthly_day_number']}")
