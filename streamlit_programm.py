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
            "KCl",
            "CaCl2",
            "Mg(CH3COO)",
            "CuSO4",
            "NaHCO3 + Na2CO3"
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

    choice = st.selectbox("Was prüfen?", ["v(r) WW ohne Salz [J]", "v(r) WW mit Salz [J]", "Debye-Länge [m]"])

    sol = st.number_input("Resultat eingeben", format="%.6e")

    if st.button("Prüfen"):

        if choice == "v(r) WW ohne Salz [J]":
            correct = -1.52e-20
        elif choice == "v(r) WW mit Salz [J]":
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
        ["Volumen Benzolmolekül [m^3]", 
         "v(r) im Vakuum [J]", 
         "v(r) in Cyclohexan [J]", 
         "v(r) in Aceton [J]", 
         "Exzesspolarisierbarkeit des Benzols im Vakuum [Cm^2/V]", 
         "Exzesspolarisierbarkeit des Benzols im Cyclohexan [Cm^2/V]", 
         "Exzesspolarisierbarkeit des Benzols im Aceton [Cm^2/V]"]
    )

    sol = st.number_input("Resultat eingeben", format="%.6e")

    values = {
        "Volumen Benzolmolekül [m^3]": 1.4738e-28,
        "v(r) im Vakuum [J]": -1.2068e-21,
        "v(r) in Cyclohexan [J]": -7.9586e-23,
        "v(r) in Aceton [J]": 8.2727e-23,
        "Exzesspolarisierbarkeit des Benzols im Vakuum [Cm^2/V]": 1.164e-23,
        "Exzesspolarisierbarkeit des Benzols im Cyclohexan [Cm^2/V]": 3.133e-23,
        "Exzesspolarisierbarkeit des Benzols im Aceton [Cm^2/V]": -3.42e-23
    }

    if st.button("Prüfen"):
        correct = values[choice]

        if abs(1 - sol / correct) <= 0.05:
            st.success("Richtig.")
        else:
            st.error("Leider falsch.")
