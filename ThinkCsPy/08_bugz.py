# # in a list of numbers, print every ith number
# def print_every(iteration, nums):
#     counter = 0
#
#     for i in nums:
#         if counter % iteration == 0:
#             print(i)
#         counter += 1
#
# print_every(3, [4, 7, 2, 10, 1, 0, 9, 6])
# # should print 4, then print 10, then print 9



# # return True if every member of the group is at least 70, otherwise return False
# def check_group(ages):
#
#     is_age_over_70 = []
#
#     for age in ages:
#         if age < 70:
#             is_age_over_70.append(False)
#         else:
#             is_age_over_70.append(True)
#
#     return all(is_age_over_70)
#
# # from test import testEqual
# #
# # # this group should not be allowed inside the bar
# group = [78, 71, 25, 84]
# check_group(group)
# # testEqual(check_group(group), False)
# #
# # # this group should also not be allowed inside the bar
# group2 = [ 2, 99 ]
# check_group(group2)
# # testEqual(check_group(group2), False)
# #
# # # this loner is allowed
# group3 = [ 99 ]
# check_group(group3)
# # testEqual(check_group(group3), True)



# def password_checker(password):
#     """
#     A valid password has no spaces,
#     and at least one non-alphabetical character
#     """
#     contains_non_alpha = False
#
#     for char in password:
#
#         if char == " ":
#             return False
#         elif not char.isalpha():
#             contains_non_alpha = True
#
#     return contains_non_alpha
#
# pw1 = "i <3 makonnen"
# print(password_checker(pw1))
# # should print False
#
# pw2 = "puzzlesareforfun"
# print(password_checker(pw2))
# # should print False
#
# pw2 = "puzzlesr4fun"
# print(password_checker(pw2))
# # should print True