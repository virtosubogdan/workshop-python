def sum(a):
    print('sum', a, b)
    # b += 1


def sum_b5(a):
    b = 5
    print('sum_b5', a, b)
    b += 1


def sum_nonlocal_before(a):
    "example"
    # nonlocal b -> SyntaxError: no binding for nonlocal 'b' found -> because b is not defined at this point
    # print('sum_nonlocal', a, b)
    # b += 1


b = 3


def sum_nonlocal_after(a):
    nonlocal b
    print('sum_nonlocal', a, b)
    b += 1


sum(1)
sum_b5(1)

# def outer():
#     out = 0
#     print('outer', out)
#     out += 1
#
#     def middle():
#         nonlocal out
#         mid = 'a'
#         print('middle', out, mid)
#         mid += 'a'
#         out += 1
#
#         def inner():
#             inn = [1]
#             nonlocal mid  # mid from the scope where inner was defined
#             mid += 'a'
#             print('inner', out, mid, inn)
#             inn.append(1)
#
#         return inner
#
#     return middle
#
#
# middle_def = outer()
# middle1_inner_def = middle_def()
# middle1_inner_def()
# middle1_inner_def()
# middle2_inner_def = middle_def()
# middle2_inner_def()
# middle2_inner_def()


# def outer():
#     out = 0
#     print('outer', out)
#     out += 1
#
#     def middle():
#         nonlocal out
#         mid = 'a'
#         print('middle', out, mid)
#         mid += 'a'
#         out += 1
#
#         def inner():
#             inn = [1]
#             nonlocal mid  # mid from the scope where inner was defined
#             mid += 'a'
#             print('inner', out, mid, inn)
#             inn.append(1)
#
#         inner()
#         inner()
#
#     middle()
#     middle()
#
#
# outer()
