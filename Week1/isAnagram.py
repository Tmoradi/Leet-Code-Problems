def isAnagram(self, s: str, t: str):
        s = sorted(s)
        t = sorted(t)
   
        return s == t
