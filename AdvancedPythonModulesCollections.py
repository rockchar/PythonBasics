from collections import Counter

sample_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]

count_dict = Counter(sample_list)
print(count_dict[2])

sample_list2 = ['a', 'a', 'hello', 'hello', 1, 1, 1, 1, 1]
count_dict = Counter(sample_list2)
print(count_dict)
print(count_dict['hello'])

sentence = ("How many times each letter appears in this sample sentence lets check using a counter . This is a sample "
            "sentence")
print(Counter(sentence))
print(sentence.split())
print(Counter(sentence.lower().split()))

'''most_common function example'''
sample_letters = 'aaaaaaaaaaaaaaaabbbccccccccccccccccccddddddddeeeeeeeeeeeeef'
c = Counter(sample_letters)
print(c.most_common(2))

