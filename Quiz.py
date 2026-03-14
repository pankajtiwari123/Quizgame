import streamlit as st

st.write(" Welcome to the Python 2nd Quiz Game")
score = 0

# Question 1
st.write("\nQ1: What is the output of print(5 + 2)?")
st.write("A.  52")
st.write("B 7")
st.write("C 10")
st.write("D Error")

ans = text_input("Enter your answer (A/B/C/D): ").upper()

if ans == "B":
    st.write(" Correct!")
    score += 1
else:
    st.write(" Wrong! Correct answer is B")
st.write("-----------------------------------------------------")  

# Question 2
st.write("\nQ2: Which keyword is used to define a function in Python?")
st.write("A func")
st.write("B define")
st.write("C def")
st.write("D function")

ans =text_input("Enter your answer (A/B/C/D): ").upper()

if ans == "C":
    st.write("Correct!")
    score += 1
else:
    st.write(" Wrong! Correct answer is C")
st.write("----------------------------------------------------")  

# Question 3
st.write("\nQ3: What is the output of print(len([1,2,3]))?")
st.write("A 2")
st.write("B 3")
st.write("C 4")
st.write("D Error")

ans = text_input("Enter your answer (A/B/C/D): ").upper()

if ans == "B":
    st.write(" Correct!")
    score += 1
elif ans == "A" or ans == "C" or ans == "D":
    st.write(" Wrong! Correct answer is B")
else:
    st.write(" Invalid input!")
st.write("----------------------------------------------------")   

# Final Score
st.write("\n Quiz Finished!")
st.write("Your score is:", score, "/ 3")

