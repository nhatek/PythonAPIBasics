# PythonAPIBasics

**Project name:** Habit Tracker

**Things I Implemented:** Requests, public API

**Habit Tracking:** https://pixe.la/

**API Documentation:** https://docs.pixe.la/

**Example graph that keeps track of my reading habit:** https://pixe.la/v1/users/nhatek/graphs/graph1.html

## How to Use:

**1. Create a user profile by declaring unique constants as shown in the example:**

*USERNAME = "username"
TOKEN = "PQ88wP1grYE2"*

Make sure your USERNAME is not already taken.
TOKEN should have at least 8 characters.

**3. Create a new graph by specifying required values in grap_config:**

*graph_config = {
"id": GRAPH_ID,
"name": "Reading",
"unit": "pages",
"type": "int",
"color": "ajisai",
}*

For further graph modification I recommend visiting the official API documentation.

**4. Run [tracker.py](http://tracker.py/) to update your graph**
