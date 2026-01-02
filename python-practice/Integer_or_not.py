def Check_Integer (N):
    if '.' not in N:
        return 'YES'
    else:
        pass

    parts = N.split('.')
    fractional_part= parts[1]
    if fractional_part.strip("0")=="":
        return "YES"
    else:
        return "NO"

T = int(input())
for _ in range(T):
    N = input()

    out_ = Check_Integer(N)
    print (out_)
