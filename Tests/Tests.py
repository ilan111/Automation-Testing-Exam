class Tests:
    # Test for Part 1
    def check_price(price):
        assert price > 1000, "Price is <= 1000"
        print("Price is greater than 1000!")

    # Test for Part 2-A
    def test_sum_of_prices(sum):
        assert sum > 2500, "Sum of prices is less or equal to 2500!"
        print("Sum of prices is larger than 2500!")

    # Test for Part 2-B
    def test_sum_of_ids(sum):
        assert sum > 5, 'Sum of ids is less or equal to 5!'
        print('Sum of ids is larger than 5!')
