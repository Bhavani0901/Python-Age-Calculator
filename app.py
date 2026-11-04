
import streamlit as st
from datetime import date
from calendar import monthrange


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered"
)


# --------------------------------
# AGE CALCULATION FUNCTION
# --------------------------------

def add_months(original_date, months):

    total_months = original_date.year * 12 + original_date.month - 1 + months

    year = total_months // 12
    month = total_months % 12 + 1

    day = min(
        original_date.day,
        monthrange(year, month)[1]
    )

    return date(year, month, day)


def calculate_age(dob, today):

    # Calculate completed years
    years = today.year - dob.year

    anniversary = add_months(dob, years * 12)

    if anniversary > today:
        years -= 1
        anniversary = add_months(dob, years * 12)

    # Calculate completed months
    months = (
        (today.year - anniversary.year) * 12
        + today.month - anniversary.month
    )

    month_anniversary = add_months(anniversary, months)

    if month_anniversary > today:
        months -= 1
        month_anniversary = add_months(anniversary, months)

    # Calculate remaining days
    days = (today - month_anniversary).days

    return years, months, days


# --------------------------------
# WEBPAGE DESIGN
# --------------------------------

st.title("🎂 Age Calculator")

st.write(
    "Calculate your exact age in years, months and days."
)

st.divider()

st.header("Enter Your Details")

# Get today's date
today = date.today()

# Date picker
dob = st.date_input(
    "Select your date of birth",
    min_value=date(1900, 1, 1),
    max_value=today,
    value=date(2000, 1, 1),
    format="DD/MM/YYYY"
)

# Calculate button
if st.button("Calculate Age", type="primary"):

    # Validate date of birth
    if dob > today:

        st.error("Future dates are not allowed!")

    else:

        # Call the age calculation function
        years, months, days = calculate_age(dob, today)

        st.divider()

        st.subheader("Your Exact Age")

        # Display age in three columns
        col1, col2, col3 = st.columns(3)

        col1.metric("Years", years)
        col2.metric("Months", months)
        col3.metric("Days", days)

        st.success(
            f"You are {years} years, "
            f"{months} months and {days} days old!"
        )

st.divider()

st.caption("Developed using Python and Streamlit")
