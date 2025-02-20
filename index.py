import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "User", "Admin"]

def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)
    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()

def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")
user_page = st.Page("pages/user/user_page.py", title="User Page", icon=":material/person:", default=(role == "User"))
admin_page = st.Page("pages/admin/admin_page.py", title="Admin Page", icon=":material/security:", default=(role == "Admin"))

account_pages = [logout_page, settings]
user_pages = [user_page]
admin_pages = [admin_page]

st.title("User Manager")
st.logo("images/crispychicken.png", icon_image="images/crispychicken.png")

page_dict = {"Account": account_pages}
if role == "User":
    page_dict["User"] = user_pages
elif role == "Admin":
    page_dict["Admin"] = admin_pages

if role:
    pg = st.navigation(page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
