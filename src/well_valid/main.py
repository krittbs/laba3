from well_valid import config
from well_valid import validators

def main() -> None:
    print("ВАЛИДАТОР ТЕХНОЛОГИЧЕСКОГО РЕЖИМА (Вариант Б, N=2)")
    print("=" * 50)
    q = w = p_res = p_bhp = h = None
    
    while True:
        print()
        print("МЕНЮ")
        print("1 — ввод параметров")
        print("2 — классификация по обводнённости")
        print("3 — режим по давлениям")
        print("4 — сводка")
        print("5 — справка")  # Упражнение 5
        print("0 — выход")
        
        choice = input("Выбор: ").strip()
        match choice:
            case "1":
                q = validators.input_bounded("Дебит жидкости Qж, м³/сут: ", "Qж", *config.Q_RANGE)
                w = validators.input_bounded("Обводнённость W, %: ", "W", *config.W_RANGE)
                p_res = validators.input_bounded("Пластовое давление Pпл, МПа: ", "Pпл", *config.P_RES_RANGE)
                p_bhp = validators.input_bounded("Забойное давление Pзаб, МПа: ", "Pзаб", *config.P_BHP_RANGE)
                h = validators.input_bounded("Глубина H, м: ", "H", *config.H_RANGE)
                print("[ok] Параметры приняты.")
            case "2":
                if w is None:
                    print("[предупреждение] Сначала введите параметры (пункт 1).")
                else:
                    print(f"W = {w:.1f}% -> {validators.classify_well(w)}")
            case "3":
                if p_res is None or p_bhp is None:
                    print("[предупреждение] Сначала введите параметры (пункт 1).")
                else:
                    status, dp = validators.check_mode(p_res, p_bhp)
                    print(f"Депрессия ΔP = {dp:.2f} МПа; режим: {status}")
                    validators.print_action(status, dp, q if q is not None else 0.0)
            case "4":
                if q is None:
                    print("[предупреждение] Сначала введите параметры (пункт 1).")
                else:
                    print(f"Qж={q:.1f} м³/сут | W={w:.1f}% | Pпл={p_res:.2f} МПа | Pзаб={p_bhp:.2f} МПа | H={h:.0f} м")
            case "5":  # Упражнение 5
                print("\n--- СПРАВОЧНАЯ ИНФОРМАЦИЯ ---")
                print("1: Ввод всех 5 технологических параметров скважины.")
                print("2: Определение типа скважины по обводненности.")
                print("3: Анализ депрессии пласта и расчет коэффициента J.")
                print("4: Вывод текущей сводки по объекту.")
                print("0: Завершение сессии.")
                print("------------------------------")
            case "0":
                print("Выход.")
                break
            case _:
                print("[ошибка] Неизвестный пункт меню.")

if __name__ == "__main__":
    main()
