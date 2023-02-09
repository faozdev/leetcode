class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0

        for e in range(0, len(s)):
            if s[e] == 'I':
                sum = sum + 1
            elif s[e] == 'V':
                if s[e-1] == 'I'and e > 0:
                    sum = sum + 3
                else:
                    sum = sum + 5
            elif s[e] == 'X':
                if s[e-1] == 'I'and e > 0:
                    sum = sum + 8
                else:
                    sum = sum + 10
            elif s[e] == 'L':
                if s[e-1] == 'X'and e > 0:
                    sum = sum + 30
                else:
                    sum = sum + 50
            elif s[e] == 'C':
                if s[e-1] == 'X'and e > 0:
                    sum = sum + 80
                else:
                    sum = sum + 100
            elif s[e] == 'D':
                if s[e-1] == 'C'and e > 0:
                    sum = sum + 300
                else:
                    sum = sum + 500
            elif s[e] == 'M':
                if s[e-1] == 'C'and e > 0:
                    sum = sum + 800
                else:
                    sum = sum + 1000
        return sum    
