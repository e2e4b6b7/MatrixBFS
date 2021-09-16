# MatrixBFS

Тестовое задание для осенней стажировки в JetBrains

## Описание алгоритма

Алгоритм принимает набор стартовых вершин и возвращает вектор, где для каждой вершины указано, из какой она достижима или то, что она не достижима. 

Алгоритм: 

1. Превращаем набор стартовых вершин в вектор, где под индексом каждой стартовой вершины значение -- её индекс, а по остальным индексам нет значений.
2. Это -- набор и метки достижимых на первой итерации
3. Затем получаем набор достижимых с метками для последующих итераций
4. Когда набор будет равен набору на предыдущей итерации, то алгоритм завершён, возвращаем набор

Получение набора с метками для следующей итерации:

1. Домножаем вектор меток на прошлой итерации на матрицу смежности в полукольце Min/Times. Получаем вектор меток для достижимых из вершин с прошлой итерации (если достижима из нескольких, то берётся меньший номер)
2. Суммируем вектор меток на прошлой итерации с вектором из прошлого пункта с помощью операции First (чтобы для уже достигнутых ранее вершин, не менялись метки)

## Описание кода

Реализация лежит в файле `bfs.py`

Тесты лежат в файле `test_bfs.py`. Запуск: `python test_bfs.py`
