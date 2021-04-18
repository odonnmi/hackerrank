
def repeatedString(s, n):
    a_count_in_substring = s.count('a')
    a_count_in_mod = s[:(n % len(s))].count('a')
    a_count = a_count_in_substring * int(n/len(s)) + a_count_in_mod 
    # string_length = int(n/len(s)) + (n % len(s) > 0)
    # print(string_length)
    # full_string = (s*string_length)[:n]
    # print(full_string)
    # a_count = full_string.count('a')
    # ass = [ a for a in full_string if a == 'a']
    # print(ass) 
    print(a_count)


if __name__ == '__main__':
    string1 = 'abc'
    letter_count = 10
    repeatedString(string1,letter_count)