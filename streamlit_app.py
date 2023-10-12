from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Bank fraud detection
## Enter details
"""


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))

def on_predict(inc, nms, pam, cam, ca, dsr):
    st.text(f"Entered data \nIncome: {inc}\nName Email Similarity: {nms}\nPrevious Address Months: {pam}\nCurrent Address Months: {cam}\nCustomer Age: {ca}\nDays Since Request: {dsr}")

income = st.slider("Income", min_value=0.0, max_value=1.0, step=0.05)
name_email_similarity= st.slider("Name and Email similarity", min_value=0.0, max_value=1.0, step=0.05)
previous_address_months = st.slider("Previous address months count", min_value=-1, max_value=500, step=1)
current_address_months = st.slider("Current address months count", min_value=-1, max_value=500, step=1)
customer_age = st.slider("Customer age in bins per decade e.g. 20-20 is 20", min_value=1, max_value=100, step=10)
days_since_request = st.slider("Days since request", min_value=0, max_value=100, step=1)

if st.button('Predict', type="primary"):
    on_predict(income, name_email_similarity, previous_address_months, current_address_months, customer_age, days_since_request)
else:
    st.write('Press the button to predict')