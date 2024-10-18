def romanToInt(s: str) -> int:
      actualValue = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
      }
      sum = 0
      for i, r in enumerate(s):
          if i + 1 == len(s):
              sum += actualValue[r]
          else:
              if actualValue[r] >= actualValue[s[i + 1]]:
                  sum += actualValue[r]
              else:
                  sum -= actualValue[r]
      return sum
