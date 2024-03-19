import streamlit as st
from datetime import datetime, timedelta

def repair_laptop(arrival_date):
    repair_date = arrival_date + timedelta(days=25)
    return repair_date

def main():
    st.title('Laptop Repair Service')
    
    # Default arrival date is the current date
    current_date = datetime.now().date()
    arrival_date = st.date_input('Arrival Date', current_date)
    
    if st.button('Repair Laptop'):
        repair_date = repair_laptop(arrival_date)
        st.write(f"Your laptop is repaired and ready to pick up on {repair_date.strftime('%Y-%m-%d')}.")

if __name__ == "__main__":
    main()
