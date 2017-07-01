def print_without_vowels(s):
                '''
                s: the string to convert
                Finds a version of s without vowels and whose characters appear in the
                same order they appear in s. Prints this version of s.
                Does not return anything
                '''
                new=[]
                vowels = ("aeiouAEIOU")
                for i in s:
                    if i not in vowels:
                        new.append(i)
                print(''.join(new))
