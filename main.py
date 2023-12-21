import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def load_data(filename):
    df = pd.read_csv(filename)
    X = df[['IW', 'IF', 'VW', 'FP']]
    y_depth = df['Depth']
    y_width = df['Width']
    return X, y_depth, y_width


def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model_depth = LinearRegression()
    model_depth.fit(X_train, y_train)
    model_width = LinearRegression()
    model_width.fit(X_train, y_train)
    return model_depth, model_width


def predict(model_depth, model_width, IW, IF, VW, FP):
    y_pred_depth = model_depth.predict([[IW, IF, VW, FP]])
    y_pred_width = model_width.predict([[IW, IF, VW, FP]])
    return y_pred_depth[0], y_pred_width[0]


def main():
    X, y_depth, y_width = load_data('ebw_data.csv')
    X_train, X_test, y_train, y_test = split_data(X, y_depth, test_size=0.2, random_state=42)
    model_depth, model_width = train_model(X_train, y_train)

    while True:
        action = input('Выберите действие:\nstart - начать работу программы\nquit - завершить работу программы\n')
        if action == 'quit':
            break
        elif action == 'start':
            while True:
                try:
                    IW = float(input("Введите IW (величина сварочного тока): "))
                    if IW < 0:
                        raise ValueError("IW должен быть неотрицательным числом")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    IF = float(input("Введите IF (ток фокусировки электронного пучка): "))
                    if IF < 0:
                        raise ValueError("IF должен быть неотрицательным числом")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    VW = float(input("Введите VW (скорость сварки): "))
                    if VW < 0:
                        raise ValueError("VW должен быть неотрицательным числом")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    FP = float(input("Введите FP (расстояние от поверхности образцов до электронно-оптической системы): "))
                    if FP < 0:
                        raise ValueError("FP должен быть неотрицательным числом")
                    break
                except ValueError as e:
                    print(e)

            y_pred_depth, y_pred_width = predict(model_depth, model_width, IW, IF, VW, FP)
            print(f'Прогноз глубины: {y_pred_depth:.2f} мм')
            print(f'Прогноз ширины: {y_pred_width:.2f} мм\n')
        else:
            print('Такой команды не существует!\nПовторите ещё раз.\n')
    print('Программа успешно завершена!')


if __name__ == '__main__':
    main()
