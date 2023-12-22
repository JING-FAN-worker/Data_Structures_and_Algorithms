def sales(cars, customers):
    customers.sort()
    cars.sort()
    car_idx = 0
    customer_idx = 0
    count = 0
    while car_idx < len(cars) and customer_idx < len(customers):
        if customers[customer_idx] >= cars[car_idx]:
            count += 1
            car_idx += 1
        customer_idx += 1
    return count

if __name__ == "__main__":
    print(sales([20, 10, 15], [11, 25, 15]))