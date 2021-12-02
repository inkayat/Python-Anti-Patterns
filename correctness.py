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

    3.Else clause on loop without a break statement

        [Anti-patttern]
        def contains_magic_number(list, magic_number):
            for i in list:
                if i == magic__number:
                    print("This list contains the magic number")
            else:
                print("This list does NOT contain the magic number")

        [Best practices]
        def contains_magic_number(list, magic_number):
            for i in list:
                if i == magic_number:
                    print("This list contains the magic number.")
                    #added break statement
                    break
            else:
                print("This list does NOT contain the magic number.")


    4.__exit__ must accept 3 arguments: type, value, traceback

       [Anti-pattern]
       class Rectangle:
           def __init__(self, width, height):
               self.width = width
               self.height = height

           def __enter__(self):
               print("in __enter__")
               return self

           def __exit__(self):
               print("in __exit__")

           def divide_by_zero(self):
               return self.width / 0

       with Rectangle(3, 4) as r:
           r.divide_by_zero()
           #__exit__ should be called but isn't

      [Best practices]
      class Rectangle:
          def __init__(self, width, height):
              self.width = width
              self.height = height

          def __enter__(self):
              print("in __enter__")
              return self

          def __exit__(self, exception_type, exception_value, traceback):
              print("in __exit__")


"""
