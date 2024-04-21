import streamlit as st

def calculate_max(a, b, c):
    return max(a, b, c)

def main():
    st.title("Maximum Calculator")

    # Input fields for three numbers
    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    # Button to calculate maximum
    if st.button("Calculate Maximum"):
        max_num = calculate_max(num1, num2, num3)
        st.write(f"The maximum of {num1}, {num2}, and {num3} is: {max_num}")

if __name__ == "__main__":
    main()
