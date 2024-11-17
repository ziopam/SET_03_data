import numpy as np
import streamlit as st
import pandas as pd
import matplotlib as plt


def main():
    st.set_page_config(layout="wide")
    uploaded_files = st.file_uploader("Загрузите файл с данными", type=["txt", "csv"], accept_multiple_files=True)

    real_area = 0.25 * np.pi + 1.25 * np.arcsin(0.8) - 1

    for file in uploaded_files:
        try:
            df = pd.read_csv(file, header=None, names=["x", "Приблизительная площадь", "Отклонение"])
            if df.isnull().values.any():
                st.error("Ошибка: Файл содержит пустые значения. Проверьте данные.")
                return

            data_fx = df[["x", "Приблизительная площадь"]].set_index("x")
            data_error = df[["x", "Отклонение"]].set_index("x")

            real_area_line = pd.DataFrame(
                {"Фактическая площадь": [real_area] * len(data_fx)}, index=data_fx.index
            )
            data_fx["Фактическая площадь"] = real_area

            st.write(file.name.rstrip('.txt'))
            columns = st.columns(2)

            with columns[0]:
                st.line_chart(data_fx, x_label="N", y_label="Приблизительная площадь")

            with columns[1]:
                st.line_chart(data_error, x_label="N", y_label="Относительное отклонение")

        except Exception as e:
            st.error(f"Ошибка при обработке файла: {e}")


if __name__ == "__main__":
    main()
