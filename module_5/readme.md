# Проект 5. Задача регрессии. Предсказание общей продолжительности поездки такси

### УСЛОВИЯ ЗАДАНИЯ
Необходимо построить модель, предсказывающую общую продолжительность поездки такси в Нью-Йорке.
Техническая задача: построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать числовой признак - время поездки такси. То есть решить задачу регрессии.
Основные цели проекта:
1. Сформировать набор данных на основе нескольких источников информации
2. Спроектировать новые признаки с помощью Feature Engineering и выявить наиболее значимые при построении модели
3. Исследовать предоставленные данные и выявить закономерности
4. Построить несколько моделей и выбрать из них наилучшую по заданной метрике
5. Спроектировать процесс предсказания времени длительности поездки для новых данных

После выполнения проекта загрузить свое решение на платформу Kaggle, поучаствовав в настоящем Data Science соревновании.

### МЕТРИКА КАЧЕСТВА
В качестве моделей в проекте используются разные модели, необходимо выбрать лучшую. Каждая модель оценивается с помощью метрики RMSLE, исходя их канонов соревнования на Kaggle. Выбранную наилучшую модель оцениваем с помощью метрики медианной абсолютной ошибкй MeAE.

### ДОСТИГНУТЫЙ РЕЗУЛЬТАТ
Наилучшие результаты среди классических методов показал градиентный бустинг над деревьями решений. Хотя набравшая большую популярность модель экстремального градиентного бустинга (XGBoost) из библиотеки xgboost показала еще более высокие результаты.
Проект загружен на Kaggle.

### ДАННЫЕ
Исходные и подгружаемые в процессе работы данные находятся в папке на гугл-диске:
https://drive.google.com/drive/folders/1rQncQkV-zDmbboAE5-B89H_UfKxVFKDe?usp=sharing