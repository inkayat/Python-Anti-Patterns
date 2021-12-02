"""
    1.Assigning a lambda expression to a variable

        [Anti-pattern]
        f = lambda x: 2 * x

        [Best practices]
        def f(x): return 2 * x

    2.Bad except clauses order

        [Anti-pattern]
        try:
            5 / 0
        except Exception as e:
            print("Exception")
        except ZeroDivisionError as e:
            print("ZeroDivisionError")

        [Best practice]
        try:
            5 / 0
        except ZeroDivisionError as e:
            print("ZeroDivisionError")
        except Exception as e:
            print("Exception")


"""
