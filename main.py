import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('ebw_data.csv')

X = df[['IW', 'IF', 'VW', 'FP']]
y_depth = df['Depth']
y_width = df['Width']

X_train, X_test, y_train_depth, y_test_depth = train_test_split(X, y_depth, test_size=0.2, random_state=42)
_, _, y_train_width, y_test_width = train_test_split(X, y_width, test_size=0.2, random_state=42)

model_depth = LinearRegression()
model_depth.fit(X_train, y_train_depth)

model_width = LinearRegression()
model_width.fit(X_train, y_train_width)


while True:
    action = input('Выберите действие:\nstart - начать работу программы\nquit - завершить работу программы\n'
                   'Ваш выбор: ')
    if action == 'quit':
        break
    elif action == 'start':
        while True:
            try:
                iw = float(input("Введите IW (величина сварочного тока): "))
                if iw < 0:
                    raise ValueError("IW должен быть неотрицательным числом")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                if_ = float(input("Введите IF (ток фокусировки электронного пучка): "))
                if if_ < 0:
                    raise ValueError("IF должен быть неотрицательным числом")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                vw = float(input("Введите VW (скорость сварки): "))
                if vw < 0:
                    raise ValueError("VW должен быть неотрицательным числом")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                fp = float(input("Введите FP (расстояние от поверхности образцов до электронно-оптической системы): "))
                if fp < 0:
                    raise ValueError("FP должен быть неотрицательным числом")
                break
            except ValueError as e:
                print(e)

        y_pred_depth = model_depth.predict([[iw, if_, vw, fp]])
        y_pred_width = model_width.predict([[iw, if_, vw, fp]])

        print(f'Прогноз глубины: {y_pred_depth[0]:.2f} мм')
        print(f'Прогноз ширины: {y_pred_width[0]:.2f} мм\n')
    else:
        print('Такой команды не существует!\nПовторите ещё раз.\n')

print('Программа успешно завершена!')
