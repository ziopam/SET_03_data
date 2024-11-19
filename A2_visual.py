import streamlit as st
import pandas as pd


def main():
    st.set_page_config(layout="wide")

    # Загрузка файла (CSV или TXT)
    uploaded_file = st.file_uploader("Загрузите CSV или TXT файл (без заголовков)", type=["csv", "txt"])

    if uploaded_file is not None:
        try:
            # Чтение файла (без заголовков)
            df = pd.read_csv(uploaded_file, header=None)

            # Переименование столбцов
            df.columns = ["n", "rand_arr_time", "reversed_arr_time", "almost_sorted_arr_time"]

            # Создание отдельных графиков
            columns = st.columns(3)
            with columns[0]:
                st.write("Случайный массив")
                st.line_chart(data=df, x="n", y="rand_arr_time", use_container_width=True)
            with columns[1]:
                st.write("Обратно отсортированный массив")
                st.line_chart(data=df, x="n", y="reversed_arr_time", use_container_width=True)
            with columns[2]:
                st.write("Почти отсортированный массив")
                st.line_chart(data=df, x="n", y="almost_sorted_arr_time", use_container_width=True)

        except Exception as e:
            st.error(f"Ошибка при обработке файла: {e}")


if __name__ == "__main__":
    main()
