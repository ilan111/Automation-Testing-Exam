import time

from HomePage import HomePage
from Tests import Tests


def part1():
    first_task = HomePage()
    first_task.open_site()
    first_task.search("macbook")
    price = first_task.print_price_and_description()
    Tests.check_price(price)
    first_task.driver_quit()


def part2a():
    second_task_a = HomePage()
    second_task_a.open_site()
    second_task_a.navigate_to_page("Computers", "Desktops")
    prices = second_task_a.summarize_prices()
    Tests.test_sum_of_prices(prices)
    second_task_a.driver_quit()


def part2b():
    second_task_b = HomePage()
    second_task_b.open_site()
    second_task_b.navigate_to_page("Computers", "Notebooks")
    ids = second_task_b.summarize_ids()
    Tests.test_sum_of_ids(ids)
    second_task_b.driver_quit()


def main():

    part1()
    time.sleep(2)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    part2a()
    time.sleep(2)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    part2b()


if __name__ == "__main__":
    main()
