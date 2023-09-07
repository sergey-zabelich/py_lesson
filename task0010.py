def calculate_results():
    # Ввод количества игр
    num_games = int(input("Введите количество игр: "))
    
    # Словарь для хранения результатов команд
    results = {}
    
    # Обработка результатов игр
    for _ in range(num_games):
        game_input = input("Кто играет? (Например: Спартак - Зенит): ").split(" - ")
        team1 = game_input[0].strip()
        team2 = game_input[1].strip()
        
        # Проверка наличия игры в правильном формате
        if team1 == "" or team2 == "":
            print("Неправильный формат ввода игры. Повторите ввод.")
            continue
        
        # Ввод результатов игры
        result_input = input("Результат игры (Голы первой команды - Голы второй команды): ")
        try:
            goals1, goals2 = map(int, result_input.split("-"))
        except ValueError:
            print("Неправильный формат ввода результатов. Повторите ввод.")
            continue
        
        # Добавление команд и их результатов в словарь
        if team1 not in results:
            results[team1] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}
        if team2 not in results:
            results[team2] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}
        
        results[team1]["games"] += 1
        results[team2]["games"] += 1
        
        if goals1 > goals2:
            results[team1]["wins"] += 1
            results[team1]["points"] += 3
            results[team2]["losses"] += 1
        elif goals1 < goals2:
            results[team2]["wins"] += 1
            results[team2]["points"] += 3
            results[team1]["losses"] += 1
        else:
            results[team1]["draws"] += 1
            results[team1]["points"] += 1
            results[team2]["draws"] += 1
            results[team2]["points"] += 1
    
    # Вывод сводной таблицы результатов
    print("| Название команды | Всего игр | Побед | Ничьих | Поражений | Всего очков |")
    print("|------------------|-----------|-------|--------|------------|-------------|")
    for team, data in results.items():
        print(f"| {team:<16} | {data['games']:^9} | {data['wins']:^5} | {data['draws']:^6} | {data['losses']:^10} | {data['points']:^11} |")

# Вызов функции для расчета результатов
calculate_results()