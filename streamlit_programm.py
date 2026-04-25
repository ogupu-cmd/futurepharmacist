import streamlit as st

st.title("Physikalische Chemie – Ü7 – Resultatkontrolle")

# ---------------- SESSION STATE ----------------
if "task" not in st.session_state:
    st.session_state.task = None

if "subtask" not in st.session_state:
    st.session_state.subtask = None

# ---------------- AUFGABE AUSWÄHLEN ----------------
st.session_state.task = st.selectbox(
    "Welche Aufgabe?",
    ["", "1b", "2b", "3b"]
)

# ===================== 1b =====================
if st.session_state.task == "1b":
    st.subheader("Aufgabe 1b")

    solut = st.selectbox(
        "Salzlösung auswählen",
        {
            "1": "KCl",
            "2": "CaCl2",
            "3": "Mg(CH3COO)",
            "4": "CuSO4",
            "5": "NaHCO3 + Na2CO3"
        }
    )

    sol = st.number_input("Ergebnis [mol/L]", format="%.6f")

    solutions = {
        "1": 0.5,
        "2": 1.5,
        "3": 1.5,
        "4": 0.4,
        "5": 0.2
    }

    if st.button("Prüfen"):
        if abs(sol - solutions[solut]) < 1e-6:
            st.success("Richtig")
        else:
            st.error("Leider falsch")

# ===================== 2b =====================
elif st.session_state.task == "2b":
    st.subheader("Aufgabe 2b")

    choice = st.selectbox("Was prüfen?", ["1", "2", "3"])

    sol = st.number_input("Resultat eingeben", format="%.6e")

    if st.button("Prüfen"):

        if choice == "1":
            correct = -1.52e-20
        elif choice == "2":
            correct = -1.34e-20
        else:
            correct = 3.13e-9

        if abs(1 - sol / correct) <= 0.05:
            st.success("Richtig.")
        else:
            st.error("Leider falsch.")

# ===================== 3b =====================
elif st.session_state.task == "3b":
    st.subheader("Aufgabe 3b")

    choice = st.selectbox(
        "Was prüfen?",
        ["1", "2", "3", "4", "5", "6", "7"]
    )

    sol = st.number_input("Resultat eingeben", format="%.6e")

    values = {
        "1": 1.4738e-28,
        "2": -1.2068e-21,
        "3": -7.9586e-23,
        "4": 8.2727e-23,
        "5": 1.164e-23,
        "6": 3.133e-23,
        "7": -3.42e-23
    }

    if st.button("Prüfen"):
        correct = values[choice]

        if abs(1 - sol / correct) <= 0.05:
            st.success("Richtig.")
        else:
            st.error("Leider falsch.")