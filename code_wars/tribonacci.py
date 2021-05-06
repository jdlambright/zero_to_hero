
def tribonacci(signature, n):
    trib = signature
    for i in range(n-2):
        result = signature[-1] + signature[-2] + signature[-3]
        trib.append(result)

    return result




tribonacci([1,1,1], 10)