import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide")

    # Загрузка нескольких файлов
    uploaded_files = st.file_uploader(
        "Загрузите CSV или TXT файлы (без заголовков)",
        type=["csv", "txt"],
        accept_multiple_files=True,
    )

    # Обработка каждого загруженного файла
    if uploaded_files:
        for file in uploaded_files:
            try:
                # Чтение файла без заголовков
                df = pd.read_csv(file, header=None)
                df.columns = ["n", "rand_arr_time", "reversed_arr_time", "almost_sorted_arr_time"]

                # Перевод времени из микросекунд в миллисекунды
                df["rand_arr_time"] /= 1000
                df["reversed_arr_time"] /= 1000
                df["almost_sorted_arr_time"] /= 1000

                # Отображение названия файла
                st.subheader(f"Графики для файла: {file.name}")

                # Создание трех графиков для текущего файла
                columns = st.columns(3)
                with columns[0]:
                    st.write("Случайный массив (время, мс)")
                    st.line_chart(data=df, x="n", y="rand_arr_time", use_container_width=True)
                with columns[1]:
                    st.write("Обратно отсортированный массив (время, мс)")
                    st.line_chart(data=df, x="n", y="reversed_arr_time", use_container_width=True)
                with columns[2]:
                    st.write("Почти отсортированный массив (время, мс)")
                    st.line_chart(data=df, x="n", y="almost_sorted_arr_time", use_container_width=True)

            except Exception as e:
                st.error(f"Ошибка при обработке файла {file.name}: {e}")

if __name__ == "__main__":
    main()
