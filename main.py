import os
from datatypes.graph import create_graph

def main():
    print("Оберіть дію:\n"
          "1. Вивести вхідний граф\n"
          "2. Виконати алгоритм Дейкстри\n"
          "3. Виконати алгоритм Флойда\n")
    graph = create_graph()

    item = int(input("Оберіть елемент Меню: "))
    match item:
        case 1:
            print("Вхідний граф")
            graph.print()
        case 2:
            print("Алгоритм Дейкстри")
            vertex = input("Оберіть стартову вершину: ")
            node_id = graph.get_node_id(vertex)
            if node_id >= 0:
                graph.print_deykstra(node_id)
        case 3:
            print("\nАлгоритм Флойда")
            graph.print_floyd()
    input("Натисніть будь-яку кнопку")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    main()

main()
