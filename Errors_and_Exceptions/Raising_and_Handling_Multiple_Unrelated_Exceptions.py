# 8.9. Raising and Handling Multiple Unrelated Exceptions
# ExceptionGroup
# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)
#
# # f()
#
#
# try:
#     f()
# except Exception as e:
#     print(f'caught {type(e)}: e')



# using except*
def g():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    g()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")