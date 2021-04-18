def hourglassSum(arr):
    # hb_high_sum = 0
    for i in range(6):
        for j in range(6):
            # print(f"{i}, {j}")
            try:
                hg_sum = (
                    arr[i][j]
                    + arr[i][j + 1]
                    + arr[i][j + 2]
                    + arr[i + 1][j + 1]
                    + arr[i + 2][j]
                    + arr[i + 2][j + 1]
                    + arr[i + 2][j + 2]
                ) 
                try:
                    if hg_sum > hg_high_sum:
                        hg_high_sum = hg_sum 
                except NameError: 
                    hg_high_sum = hg_sum
                print(f"hourglass sum {hg_high_sum}")
            except IndexError:
                pass
    return hg_high_sum
             


if __name__ == "__main__":
    twod_array = []
    twod_array.append(list(map(int, "1 1 1 0 0 0".split())))
    twod_array.append(list(map(int, "0 1 0 0 0 0".split())))
    twod_array.append(list(map(int, "1 1 1 0 0 0".split())))
    twod_array.append(list(map(int, "0 0 2 4 4 0".split())))
    twod_array.append(list(map(int, "0 0 0 2 0 0".split())))
    twod_array.append(list(map(int, "0 0 1 2 4 0".split())))

    print(twod_array)
    hourglassSum(twod_array)