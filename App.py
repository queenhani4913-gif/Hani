
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Hub",
    page_icon="🧵",
    layout="wide"
)

# ---------- Custom Design ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #F5FAF8, #F1F5FB);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #17324D, #20566A);
}
[data-testid="stSidebar"] * {
    color: white;
}
.hero {
    padding: 28px;
    border-radius: 18px;
    color: white;
    background: linear-gradient(
        110deg, #17324D, #138A8A, #57B99A
    );
    margin-bottom: 20px;
}
.hero h1 {
    margin: 0;
    font-size: 36px;
}
.hero p {
    font-size: 17px;
}
.metric-card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #DDE8E7;
    box-shadow: 0 4px 14px #17324D10;
}
.metric-label {
    color: #567080;
    font-size: 14px;
}
.metric-value {
    color: #17324D;
    font-size: 27px;
    font-weight: bold;
}
div.stButton > button {
    background: #138A8A;
    color: white;
    border-radius: 9px;
    border: none;
}
div.stButton > button:hover {
    background: #0D6E70;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ---------- Sidebar ----------
st.sidebar.title("🧵 Textile Hub")
st.sidebar.caption("Your Textile Learning Workspace")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "Fiber Explorer",
        "Production Calculator",
        "Sustainability"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎨 Color Palette")
st.sidebar.markdown("🟦 Navy Blue: `#17324D`")
st.sidebar.markdown("🟩 Teal: `#138A8A`")
st.sidebar.markdown("🌿 Mint: `#DDF4EC`")
st.sidebar.markdown("🟨 Gold: `#E7B65C`")


# ---------- Reusable Functions ----------
def hero(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def metric(label, value, detail):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-label">{detail}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------- Dashboard ----------
if page == "Dashboard":

    hero(
        "Textile Hub",
        "Explore textile fibers, production and sustainability."
    )

    st.subheader("Welcome to Your Textile Workspace")

    st.write(
        "Textile Hub is a simple educational application "
        "designed for textile engineering students. "
        "Learn about fibers, calculate fabric production "
        "and explore sustainable manufacturing."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric("Fiber Families", "3", "Natural and man-made")

    with c2:
        metric("Production Steps", "6", "Fiber to finished fabric")

    with c3:
        metric("Calculator", "Live", "Fabric area estimate")

    with c4:
        metric("Main Focus", "Green", "Sustainable textiles")

    st.markdown("---")
    left, right = st.columns(2)

    with left:
        st.subheader("🏭 Textile Production Journey")

        steps = [
            "1. Fiber Preparation",
            "2. Spinning",
            "3. Yarn Preparation",
            "4. Weaving or Knitting",
            "5. Dyeing and Finishing",
            "6. Inspection and Packing"
        ]

        for step in steps:
            st.markdown(f"- {step}")

    with right:
        st.subheader("📌 Textile Facts")

        st.info(
            "Cotton is a natural cellulosic fiber "
            "commonly used in clothing."
        )

        st.success(
            "Polyester is a synthetic fiber known "
            "for durability and wrinkle resistance."
        )

        st.warning(
            "Reducing water, energy and material waste "
            "can improve textile sustainability."
        )


# ---------- Fiber Explorer ----------
elif page == "Fiber Explorer":

    hero(
        "Fiber Explorer",
        "Explore the properties and uses of textile fibers."
    )

    fibers = {
        "Cotton": {
            "Type": "Natural cellulosic",
            "Source": "Cotton plant",
            "Properties": "Soft and breathable",
            "Uses": "T-shirts, denim and towels"
        },
        "Wool": {
            "Type": "Natural protein",
            "Source": "Sheep and other animals",
            "Properties": "Warm and resilient",
            "Uses": "Sweaters, coats and blankets"
        },
        "Silk": {
            "Type": "Natural protein",
            "Source": "Silkworm cocoon",
            "Properties": "Smooth and lustrous",
            "Uses": "Scarves and dresses"
        },
        "Polyester": {
            "Type": "Synthetic",
            "Source": "Polymer-based manufacture",
            "Properties": "Strong and quick-drying",
            "Uses": "Sportswear and blended fabrics"
        },
        "Viscose": {
            "Type": "Regenerated cellulosic",
            "Source": "Processed plant cellulose",
            "Properties": "Soft with good drape",
            "Uses": "Dresses, blouses and linings"
        },
        "Nylon": {
            "Type": "Synthetic",
            "Source": "Polyamide polymer",
            "Properties": "Lightweight and abrasion-resistant",
            "Uses": "Activewear, hosiery and bags"
        }
    }

    selected = st.selectbox(
        "Select a textile fiber",
        list(fibers.keys())
    )

    info = fibers[selected]

    st.subheader(f"🧶 {selected} Fiber")

    a, b = st.columns(2)

    with a:
        st.markdown("### Fiber Information")
        st.write(f"**Type:** {info['Type']}")
        st.write(f"**Source:** {info['Source']}")

    with b:
        st.markdown("### Characteristics")
        st.write(f"**Properties:** {info['Properties']}")
        st.write(f"**Common Uses:** {info['Uses']}")

    st.markdown("---")
    st.subheader("Compare All Fibers")

    df = pd.DataFrame([
        {"Fiber": name, **details}
        for name, details in fibers.items()
    ])

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "Fiber properties vary with grade, construction, "
        "blending and finishing."
    )


# ---------- Production Calculator ----------
elif page == "Production Calculator":

    hero(
        "Production Calculator",
        "Estimate usable material and fabric area."
    )

    st.write(
        "Enter the available material mass, estimated process "
        "loss and fabric weight to calculate an approximate area."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        mass = st.number_input(
            "Input Mass (kg)",
            min_value=0.0,
            value=500.0,
            step=10.0
        )

    with c2:
        loss = st.number_input(
            "Process Loss (%)",
            min_value=0.0,
            max_value=100.0,
            value=4.0,
            step=0.5
        )

    with c3:
        gsm = st.number_input(
            "Fabric Weight (GSM)",
            min_value=1.0,
            value=180.0,
            step=5.0
        )

    usable_mass = mass * (1 - loss / 100)
    area = usable_mass * 1000 / gsm

    st.markdown("---")
    st.subheader("📊 Estimated Results")

    r1, r2, r3 = st.columns(3)

    with r1:
        metric(
            "Usable Mass",
            f"{usable_mass:,.2f} kg",
            "After estimated process loss"
        )

    with r2:
        metric(
            "Fabric Area",
            f"{area:,.2f} m²",
            "Estimated square metres"
        )

    with r3:
        metric(
            "100 m² Units",
            f"{area / 100:,.2f}",
            "Equivalent area units"
        )

    st.markdown("### Formula")

    st.latex(
        r"\text{Usable Mass} = "
        r"\text{Input Mass}\times"
        r"\left(1-\frac{\text{Loss \%}}{100}\right)"
    )

    st.latex(
        r"\text{Area (m}^2\text{)} = "
        r"\frac{\text{Usable Mass (kg)}\times1000}"
        r"{\text{GSM (g/m}^2\text{)}}"
    )

    st.caption(
        "This is a simplified educational estimate. "
        "Actual production depends on fabric construction, "
        "width, moisture and process conditions."
    )


# ---------- Sustainability ----------
elif page == "Sustainability":

    hero(
        "Sustainability Corner",
        "Discover ways to make textile manufacturing more responsible."
    )

    st.subheader("♻️ Sustainability Improvement Areas")

    topics = {
        "Water Efficiency":
            "Monitor water use and investigate suitable water reuse.",
        "Energy Efficiency":
            "Maintain machinery and monitor energy consumption.",
        "Material Waste":
            "Improve cutting efficiency and reuse suitable offcuts.",
        "Chemical Management":
            "Follow safety data sheets and wastewater treatment rules.",
        "Product Durability":
            "Encourage long-lasting fabrics and responsible product design."
    }

    for title, description in topics.items():
        with st.expander(title):
            st.write(description)

    st.markdown("---")
    st.subheader("Create an Action Plan")

    focus = st.selectbox(
        "Choose a focus area",
        list(topics.keys())
    )

    target = st.text_input(
        "Write an improvement target",
        placeholder="Example: Record water use for each dyeing batch"
    )

    if st.button("Create Action Summary"):

        if target.strip():
            st.success(
                f"Focus Area: {focus}\n\n"
                f"Target: {target.strip()}"
            )
        else:
            st.warning("Please enter an improvement target.")


# ---------- Footer ----------
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#718391;">
        Textile Hub | Built with Streamlit 🧵
        <br>
        Educational project for textile engineering students
    </div>
    """,
    unsafe_allow_html=True
)
