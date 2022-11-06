def gamma(nums):
    ret = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        n = nums[i]
        if n == 1:
            ret[i] = 2
        elif n == 2:
            ret[i] = 6
        elif n == 6:
            ret[i] = 5
        elif n == 5:
            ret[i] = 1
        else:
            ret[i] = n
    return ret


def delta(nums):
    ret = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        n = nums[i]
        if n == 2:
            ret[i] = 3
        elif n == 3:
            ret[i] = 5
        elif n == 5:
            ret[i] = 6
        elif n == 6:
            ret[i] = 2
        else:
            ret[i] = n
    return ret


# gamma^4 = id = delta^4, gamma^5 = gamma, delta^5 = delta
# we need not go above 4
all = []
for g1 in range(4):
    for d1 in range(4):
        for g2 in range(4):
            for d2 in range(4):
                for g3 in range(4):
                    for d3 in range(4):
                        for g4 in range(4):
                            for d4 in range(4):
                                nums = [1, 2, 3, 4, 5, 6]
                                gen = [g1, d1, g2, d2, g3, d3, g4, d4]
                                out = "id ="

                                for i in range(7, -1, -1):
                                    for j in range(gen[i]):
                                        if i % 2 == 1:
                                            nums = delta(nums)
                                            #out = "d o " + out
                                        else:
                                            nums = gamma(nums)
                                            #out = "g o " + out
                                    if gen[i] > 0:
                                        if i % 2 == 1:
                                            out = "d^" + str(gen[i]) + " o " + out
                                        else:
                                            out = "g^" + str(gen[i]) + " o " + out

                                if not nums in all:
                                    all.append(nums)
                                    print(out, nums)
                                
print(len(all), 120 - len(all), " missing")
