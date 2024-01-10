import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Retail Analytics")
widget_counter = 0

cols1 = st.columns(2)
with cols1[0]:

    @st.cache_data
    def load_data():
        return pd.DataFrame(
            {
                "Day": ["Saturday", "Sunday", "Wednesday", "Thursday", "Monday", "Friday", "Tuesday"],
                "Sales": [16660, 16650, 10260, 10100, 9950, 9550, 9540],
            }
        )

    st.checkbox("Use container width", value=False, key="use_container_width_checkbox")

    df = load_data()

    fig, ax = plt.subplots()
    ax.bar(df["Day"], df["Sales"])

    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Sales")
    ax.set_title("Sales for Each Day of the Week")
    fig.set_facecolor('black')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)

with cols1[1]:
    labels = ['Cheese Burger', 'Classic Burger', 'Veggie Burger', 'Supreme Burger', 'Chocolate Milkshake', 'Coffee',
              'Coke', 'Soda', 'Strawberry Milkshake', 'Tea', 'Water']
    sizes = [18.01, 16.5, 15.6, 11.64, 6.45, 6.08, 4.6, 4.61, 7.35, 6.18, 2.98]
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # Adjusted explode list to match the length of sizes

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    fig1.set_facecolor('black')
    for text in ax1.texts:
        text.set_color('white')

    st.pyplot(fig1)

cols2 = st.columns(2)
with cols2[0]:
    labels = ['Cheese Burger', 'Classic Burger', 'Veggie Burger', 'Supreme Burger', 'Chocolate Milkshake', 'Coffee',
              'Coke', 'Soda', 'Strawberry Milkshake', 'Tea', 'Water']
    sizes = [18.01, 16.5, 15.6, 11.64, 6.45, 6.08, 4.6, 4.61, 7.35, 6.18, 2.98]
    categories = ['food', 'food', 'food', 'food', 'drink', 'drink', 'drink', 'drink', 'drink', 'drink', 'drink']

    df = pd.DataFrame({'label': labels, 'size': sizes, 'category': categories})

    df_sorted = df.sort_values(by='size', ascending=False)

    food_data = df_sorted[df_sorted['category'] == 'food']
    drink_data = df_sorted[df_sorted['category'] == 'drink']

    fig, ax = plt.subplots()
    bar_width = 0.35

    bar_food = ax.bar(food_data['label'], food_data['size'], bar_width, label='Food')
    bar_drink = ax.bar(drink_data['label'], drink_data['size'], bar_width, label='Drink', alpha=0.7)

    ax.set_xlabel('Menu', fontstyle='italic')
    ax.set_ylabel('Sales')
    ax.set_title('Food and Drink Comparison')
    ax.legend()
    fig.set_facecolor('black')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    plt.xticks(rotation=45, ha='right')

    st.pyplot(fig)

with cols2[1]:
    widget_counter = 0

    @st.cache_data
    def load_data():
        return pd.DataFrame(
            {
                "Menu": ["Cheese Burger", "Classic Burger", "Supreme Burger"],
                "4 man": [27.33, 22.31, 72.48],
                "5 man": [24.62, 22.26, 72.63],
                "6 man": [23.85, 22.44, 72.88],
                "7 man": [22.95, 22.47, 72.83],
                "8 man": [22.44, 22.43, 72.87],
                "9 man": [21.19, 22.35, 72.76],
                "10 man": [22.53, 22.50, 72.84],
            }
        )

    def get_unique_key():
        global widget_counter
        widget_counter += 1
        return f"use_container_width_{widget_counter}"

    st.checkbox("Use container width", value=False, key=f"{get_unique_key()}_checkbox")

    df = load_data()
    df = df[['Menu'] + sorted(df.columns[1:], key=lambda x: int(x.split()[0]))]
    df_t = df.set_index('Menu').T
    st.line_chart(df_t)

cols3 = st.columns(2)
with cols3[0]:
    @st.cache_data
    def load_data():
        return pd.DataFrame(
            {
                "Menu": ["Cheese Burger", "Classic Burger", "Supreme Burger"],
                "Average time 4 Man": [27.33, 22.31, 72.48],
                "Average time 5 Man": [24.62, 22.26, 72.63],
                "Average time 6 Man": [23.85, 22.44, 72.88],
                "Average time 7 Man": [22.95, 22.47, 72.83],
                "Average time 8 Man": [22.44, 22.43, 72.87],
                "Average time 9 Man": [21.19, 22.35, 72.76],
                "Average time 10 Man": [22.53, 22.50, 72.84],
            }
        )

    st.checkbox("Use container width", value=False, key="use_container_width")

    df = load_data()

