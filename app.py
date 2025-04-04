import streamlit as st
import pandas as pd
import datetime
import pytz

# Set timezone to Pakistan (Karachi)
pakistan_tz = pytz.timezone('Asia/Karachi')
current_time = datetime.datetime.now(pakistan_tz)
current_date = current_time.date()

# ✅ Set Page Config
st.set_page_config(page_title="CM Gizri Roster", layout="wide")

# ✅ Load Data Function
def load_data():
    return pd.DataFrame([
        {   
            "Supervisor": "ZAHID HUSSAIN",
            "Emp#": "80023543",
            "Task": "CM",
            "Lineman": "M.YASIR",
            "Lineman_Emp#": "80022006",
            "Fitter": "MUHAMMAD FAHIM",
            "Fitter_Emp#": "80023263",
            "Karkun": "MIRZA FAIZAN",
            "Karkun_Emp#": "1170",
            "Off_Day": "Sunday",
            "Duty_Time": "M,M,M,M,M,   Mon-Sat"
        },
  {
    "Supervisor": "M.IRFAN ARAIN",
    "Emp#":" 80023407",
    "Task": "CM",
    "Lineman": "MUHAMMAD NASIR ALI",
    "Lineman_Emp#": "80022310",
    "Fitter": "IMRAN ALI",
    "Fitter_Emp#": "80022216",
    "Karkun": "ARSHAD",
    "Karkun_Emp#": "SE-7121",
    "Off_Day": "Tuesday",
    "Duty_Time":"M,M,M,M,M,    Wed-Mon"
  },
  {
    "Supervisor": "RIASAT ALI",
    "Emp#": "4599",
    "Task": "CM",
    "Lineman": "ATTA MOHAMMAD BALOCH",
    "Lineman_Emp#": "14541",
    "Fitter": "FAROOQ",
    "Fitter_Emp#": "80023268",
    "Karkun": "BABOO HAROON",
    "Karkun_Emp#": "11993",
    "Off_Day": "Friday",
    "Duty_Time":"M,M,M,M,M,   Sat-Thu"
  },
  {
    "Supervisor": "WASEEM-UR-REHMAN",
    "Emp#": "80023743",
    "Task": "CM",
    "Lineman": "ARIF HUSSAIN",
    "Lineman_Emp#": "80022463",
    "Fitter": "VACANT",
    "Karkun": "SAJJAD",
    "Karkun_Emp#": "HK-574",
    "Off_Day": "Monday",
    "Duty_Time":"M,E,N,M,E,    Tue-Sun"
  },
  {
    "Supervisor": "AKHTAR HUSSAIN",
    "Emp#":" 8970",
    "Task": "CM",
    "Lineman": "MUHAMMAD ASIF",
    "Lineman_Emp#": "80022304",
    "Fitter": "NAZEER AHMED",
    "Fitter_Emp#": "80022037",
    "Karkun": "MUHAMMAD SHAHID",
    "Karkun_Emp#":" 6598",
    "Off_Day": "Sunday",
    "Duty_Time":"E,E,E,E,E,   Mon-Sat"
  },

  {
    "Supervisor": "SHAZAIB AHMED",
    "Emp#": "80023818",
    "Task": "CM",
    "Lineman": "YASIR KHAN",
    "Lineman_Emp#": "80021985",
    "Fitter": "SHAHNAWAZ",
    "Fitter_Emp#": "80022870",
    "Karkun": "ARSHAD",
    "Karkun_Emp#": "P-0056",
    "Off_Day": "Friday",
    "Duty_Time":"E,E,E,E,E,    Sat-Thu"
  },
  {
    "Supervisor": "SHEHZAD AHMED",
    "Emp#": "80023729",
    "Task": "CM",
    "Lineman": "MUHAMMAD DANISH",
    "Lineman_Emp#": "80022173",
    "Fitter": "MOHAMMAD ASIM",
    "Fitter_Emp#":" 5726",
    "Karkun": "MUHAMMAD LUQMAN",
    "Karkun_Emp#": "P-1913",
    "Off_Day": "Sunday",
    "Duty_Time":"N,M,E,N,M,   Mon-Sat"
  },
  {
    "Supervisor": "MUHAMMAD ZEESHAN",
    "Emp#": "80023745",
    "Task": "CM",
    "Lineman": "NOMAN AHMED",
    "Lineman_Emp#": "80022548",
    "Fitter": "MUHAMMAD ADIL BHATI",
    "Fitter_Emp#": "80022286",
    "Karkun": "DANISH AHMED",
    "Karkun_Emp#": "MM-6598",
    "Off_Day": "Monday",
    "Duty_Time":"N,M,E,N,M,   Tue-Sun"
  }
  ,
  {
    "Supervisor": "WAJID SOMROO",
    "Emp#": "80018698",
    "Task": "CM",
    "Lineman": "MUHMMAD NADEEM",
    "Lineman_Emp#": "14316",
    "Fitter": "WAQAR AHMED",
    "Fitter_Emp#":" 10801",
    "Karkun": "IMRAN KHAN",
    "Karkun_Emp#": "0652",
    "Off_Day": "Wednesday",
    "Duty_Time":"M,E,N,M,E,   Thu-Tue"
  },
  {
    "Supervisor": "MASOOD ALI",
    "Emp#": "80025132",
    "Task": "CM",
    "Lineman": "FARHAN",
    "Lineman_Emp#": "80022281",
    "Fitter": "ABDUL QADIR",
    "Fitter_Emp#": "80022283",
    "Karkun": "QADIR BUX",
    "Karkun_Emp#": "P-0892",
    "Off_Day": "Saturday",
    "Duty_Time":"E,N,M,E,N,    Mon-Fri"
  },
  {
    "Supervisor": "ALI REHAN",
    "Emp#":" 80023733",
    "Task": "CM",
    "Lineman": "ABDUL HAMEED BALOCH",
    "Lineman_Emp#": "80022318",
    "Fitter": "SYED ZAMEER SHAH",
    "Fitter_Emp#": "15215",
    "Karkun": "SUALEH KHAN",
    "Karkun_Emp#": "P-1934",
    "Off_Day": "Sunday",
    "Duty_Time":"M,E,M,M,E,    Mon-Sat"
  }
  ,
  {
    "Supervisor": "MUHAMMAD NASIR",
    "Emp#": "80023438",
    "Task": "CM",
    "Lineman": "SHAHZAD ABBASI",
    "Lineman_Emp#": "80022442",
    "Fitter": "MUHAMMAD FAIZ",
    "Fitter_Emp#": "80023269",
    "Karkun": "MUHAMMAD LAIQ",
    "Karkun_Emp#": "P-1942",
    "Off_Day": "Monday",
    "Duty_Time":"E,N,M,E,N,    Tue-Sun"
  }
  ,
  {
    "Supervisor": "M.ANUS",
    "Emp#": "80023960",
    "Task": "CM",
    "Lineman": "NASEEM ANJUM",
    "Lineman_Emp#": "80023135",
    "Fitter": "AQIL AHMED",
    "Fitter_Emp#": "80023039",
    "Karkun": "KASHIF AHMAD KHAN",
    "Karkun_Emp#": "HK-716",
    "Off_Day": "Sunday",
    "Duty_Time":"M,M,M,M,M,   Mon-Sat"
  }
  ,
  {
    "Supervisor": "DIYAR GUL",
    "Emp#":" 80023098",
    "Task": "CM",
    "Lineman": "SARDAR",
    "Lineman_Emp#": "80023763",
    "Fitter": "UMER FAROOQ",
    "Fitter_Emp#": "7997",
    "Karkun": "MOHAMMAD ATIF",
    "Karkun_Emp#": "C-2850",
    "Off_Day": "Wednesday",
    "Duty_Time":"E,N,M,E,N,   Thu-Tue"
  },
  {
    "Supervisor": "MUHAMMAD YAMEEN",
    "Emp#":" 80018664",
    "Task": "CM",
    "Lineman": "CHANZAIB",
    "Lineman_Emp#": "11917",
    "Fitter": "JUNAID",
    "Fitter_Emp#": "80022260",
    "Karkun": "IRFAN AHMED KHAN",
    "Karkun_Emp#": "C-2835",
    "Off_Day": "Thursday",
    "Duty_Time":"E,N,M,E,N,   Fri-Wed"
  },
  {
    "Supervisor": "SHABBER",
    "Emp#":" 80023546",
    "Task": "CM",
    "Lineman": "MUQARRAM SHAH",
    "Lineman_Emp#":" 8698",
    "Fitter": "NOOR HASAN",
    "Karkun": "FARAZ",
    "Karkun_Emp#": "SE-7123",
    "Off_Day": "Wednesday",
    "Duty_Time":"N,M,E,N,M,   Thu-Tue",
  },
  {
    "Supervisor": "ALTAF",
    "Emp#": "12592",
    "Task": "CM",
    "Lineman": "none",
    "Lineman_Emp#": "",
    "Fitter": "none",
    "Fitter_Emp#": "none",
    "Karkun": "none",
    "Karkun_Emp#": "none",
    "Off_Day": "Sunday",
    "Duty_Time":"E,N,N,E,N,   Mon-Sat"
  },
  {
    "Supervisor": "MANSOOB",
    "Emp#": "80025358",
    "Task": "GIS",
    "Lineman": "none",
    "Lineman_Emp#": "none",
    "Fitter": "none",
    "Fitter_Emp#": "none",
    "Karkun": "none",
    "Karkun_Emp#": "none",
    "Off_Day": "Sunday",
    "Duty_Time":"M,M,M,M,M,   Mon-Sat",
  },
  {
    "Supervisor": "NOMAN",
    "Emp#": "80010300",
    "Task": "SI MAINT",
    "Lineman": "none",
    "Lineman_Emp#": "none",
    "Fitter": "none",
    "Fitter_Emp#": "none",
    "Karkun": "none",
    "Karkun_Emp#": "none",
    "Off_Day": "none",
    "Duty_Time":"none",
  },
  {
    "Supervisor": "NADEEM SARWAR",
    "Emp#": "80024426",
    "Task": "CM",
    "Lineman": "SIRAJ",
    "Lineman_Emp#": "80023649",
    "Fitter": "IMRAN BALOCH",
    "Fitter_Emp#": "80022614",
    "Karkun": "ARIF HUSSAIN",
    "Karkun_Emp#": "1157",
    "Off_Day": "Thursday",
    "Duty_Time":"N,M,E,N,M,   Fri-Wed",
  },
  {
    "Supervisor": "ZEESHAN SHAIKH",
    "Emp#": "80010182",
    "Task": "CM",
    "Lineman": "M. SULEMAN",
    "Lineman_Emp#": "11081",
    "Fitter": "MUHAMMAD ASHFAQ",
    "Fitter_Emp#": "80022868",
    "Karkun": "MUHAMMAD KAMRAN",
    "Karkun_Emp#": "MMA-4693",
    "Off_Day": "Thursday",
    "Duty_Time":"M,E,N,M,E,   Fri-Wed",
  },
  {
    "Supervisor": "NABEEL",
    "Emp#":" 14684",
    "Task": "CM",
    "Lineman": "MUHAMMAD DANISH",
    "Lineman_Emp#": "80022618",
    "Fitter": "ZAFAR IQBAL",
    "Fitter_Emp#":" 80023286",
    "Karkun": "JOHN",
    "Karkun_Emp#": "241",
    "Off_Day": "Saturday",
    "Duty_Time":"N,M,E,N,M,   Sun-Fri",
  },
  {
    "Supervisor": "ALFRED YOUSAF",
    "Emp#": "80014989",
    "Task": "CM",
    "Lineman": "ZUBAIR ASLAM",
    "Lineman_Emp#": "80021850",
    "Fitter": "MUHAMMAD ADNAN",
    "Fitter_Emp#": "80022285",
    "Karkun": "VISHAL MUNAWAR",
    "Karkun_Emp#": "F-KE-0605",
    "Off_Day": "Sunday",
    "Duty_Time":"E,N,N,E,N,   Mon-Sat",
  },
  {
    "Supervisor": "IMRAN KHAN",
    "Emp#":" 80023400",
    "Task": "CM",
    "Lineman": "AKBER HUSSAIN",
    "Lineman_Emp#":" 80022050",
    "Fitter": "SAMEER",
    "Fitter_Emp#":" 80021732",
    "Karkun": "KHALID",
    "Karkun_Emp#":"C-2894",
    "Off_Day": "Saturday",
    "Duty_Time":"M,E,N,M,E,   Sun-Fri",

    
  },
        # Add more data here...
    ])

# ✅ Load Data
data = load_data()

# ✅ Sidebar for Navigation
with st.sidebar:
    st.image("https://vtlogo.com/wp-content/uploads/2020/03/k-electric-vector-logo.png", width=150)
    selected_date = st.date_input("📅 Select Date", current_date, min_value=datetime.date(2025, 3, 30), max_value=datetime.date(2025, 5, 3))
    view_option = st.selectbox("🔍 Search By:", ["All Teams", "Supervisor", "Lineman", "Fitter", "Karkun", "Emp#"])

    
    
    if view_option != "All Teams":
        selected_name = st.selectbox(f"Select {view_option}:", [""] + data[view_option].dropna().unique().tolist())

# ✅ Display Titles
st.markdown("<h3 style='text-align: center; color:#3498db;'>📋 DUTY ROSTER - CM GIZRI</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:#3256db;'>👤 DGM CM: Mr. Rehan Murtaza | 🏢 Manager CM: Mr. Sajid Mehmood</h5>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>⏰ Current Time in Karachi: {current_time.strftime('%I:%M %p')}</p>", unsafe_allow_html=True)

# ✅ Filter Teams Based on Selection
if view_option == "All Teams":
    filtered_data = data
else:
    filtered_data = data[data[view_option] == selected_name] if selected_name else data

# ✅ Display Teams
st.markdown(f"<h5 style='text-align: center;'>📆 Roster for {selected_date.strftime('%A, %d %B %Y')}</h5>", unsafe_allow_html=True)

for _, row in filtered_data.iterrows():
    with st.expander(f"📌 {row['Supervisor']} (Emp#: {row['Emp#']})"):
        st.markdown(f"**🛠 Task:** {row['Task']}")
        st.markdown(f"**👷 Lineman:** {row['Lineman']} (Emp#: {row['Lineman_Emp#']})")
        st.markdown(f"**🔧 Fitter:** {row['Fitter']} (Emp#: {row['Fitter_Emp#']})")
        st.markdown(f"**📌 Karkun:** {row['Karkun']} (Emp#: {row['Karkun_Emp#']})")
        st.markdown(f"**📅 Off Day:** {row['Off_Day']}")
        st.markdown(f"**⏰ Duty Time:** {row['Duty_Time']}")

# ✅ Add a Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color:gray;'>© 2025 K-Electric - CM Gizri Roster</p>", unsafe_allow_html=True)
