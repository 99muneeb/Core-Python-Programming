# def list_number(items):
#     cunts = 0
#     for x in items:
#         if len(x) > 1 and x[1] == x[-1]:
#             cunts += 1
#     return cunts


# print(list_number(['abc', 'xyz', 'aba', '1221']))
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'aya', 'aba', '1221']))
