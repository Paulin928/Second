import pandas as pd

def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        exit()
    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {file_path} пуст.")
        exit()
    except pd.errors.ParserError:
        print(f"Ошибка: Ошибка при чтении файла {file_path}.")
        exit()

def calculate_total_revenue(data):
    return data['Общая стоимость'].sum()

def find_most_sold_product(data):
    product_sales = data.groupby('Название товара')['Количество продаж'].sum()
    most_sold_product = product_sales.idxmax()
    most_sold_quantity = product_sales.max()
    return most_sold_product, most_sold_quantity

def find_product_with_highest_revenue(data):
    product_revenue = data.groupby('Название товара')['Общая стоимость'].sum()
    highest_revenue_product = product_revenue.idxmax()
    highest_revenue = product_revenue.max()
    return highest_revenue_product, highest_revenue

def generate_report(data):
    total_revenue = calculate_total_revenue(data)
    product_sales = data.groupby('Название товара')['Количество продаж'].sum()
    product_revenue = data.groupby('Название товара')['Общая стоимость'].sum()
    
    report = pd.DataFrame({
        'Количество проданных единиц': product_sales,
        'Общая выручка': product_revenue,
        'Доля в общей выручке (%)': (product_revenue / total_revenue) * 100
    }).sort_values(by='Общая выручка', ascending=False)
    
    return report, total_revenue

def main():
    file_path = 'C:\\SynthaxeCode\\devoir.csv'
    
    # Считать данные из CSV файла
    data = read_csv(file_path)
    
    # 1. Рассчитать общую выручку магазина
    total_revenue = calculate_total_revenue(data)
    print(f"Общая выручка магазина: {total_revenue:.2f} руб.")

    # 2. Найти товар, который был продан наибольшее количество раз
    most_sold_product, most_sold_quantity = find_most_sold_product(data)
    print(f"Товар, который был продан наибольшее количество раз: {most_sold_product} (Количество: {most_sold_quantity})")

    # 3. Найти товар, который принес наибольшую выручку
    highest_revenue_product, highest_revenue = find_product_with_highest_revenue(data)
    print(f"Товар, который принес наибольшую выручку: {highest_revenue_product} (Выручка: {highest_revenue:.2f} руб.)")

    # 4. Составить отчет
    report, total_revenue = generate_report(data)
    print("\nОтчет о продажах магазина:")
    print(report)

    # Сохранить отчет в CSV файл
    report.to_csv('отчет_о_продажах_магазина.csv', index=True, encoding='utf-8-sig')
    print("\nОтчет сохранен в файл 'отчет_о_продажах_магазина.csv'.")

if __name__ == "__main__":
    main()
    ile_path = 'sales_data.csv'
    sales_data = read_sales_data(file_path)

    if sales_data:
        report = generate_report(sales_data)
        print_report(report)