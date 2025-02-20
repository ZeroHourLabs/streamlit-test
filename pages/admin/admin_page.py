import streamlit as st
from streamlit_calendar import calendar

st.title("Admin Page")

calendar_options = {
    "editable": True,
    "selectable": True,
    "themeSystem": "bootstrap5",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,resourceTimelineDay",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
    "initialView": "dayGridMonth",
    "resourceGroupField": "building",
    "resources": [
        {"id": "a", "building": "Building A", "title": "Building A"},
        {"id": "b", "building": "Building A", "title": "Building B"},
        {"id": "c", "building": "Building B", "title": "Building C"},
        {"id": "d", "building": "Building B", "title": "Building D"},
        {"id": "e", "building": "Building C", "title": "Building E"},
        {"id": "f", "building": "Building C", "title": "Building F"},
    ],
}
calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "a",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
        "resourceId": "b",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
        "resourceId": "a",
    }
]
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    .fc-daygrid-event {
        background-color: #007bff !important;
        color: white !important;
        border-radius: 5px !important;
        padding: 5px !important;
    }
    .fc-toolbar {
        background-color: #f8f9fa !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    .fc-button-primary {
        background-color: #007bff !important;
        border: none !important;
    }
    .fc-button-primary:hover {
        background-color: #0056b3 !important;
    }
"""

calendar_html = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar',
)

st.write(calendar)

