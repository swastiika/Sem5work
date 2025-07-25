def SeqLFU(arr, fsize):
    cache = []  # List of [page, frequency]
    counter = 0
    for e in arr:
        pages = [x[0] for x in cache]
        if e in pages:
            for k in cache:
                if k[0] == e:
                    k[1] += 1
            counter += 1  # Hit
        else:
            if len(cache) < fsize:
                cache.append([e, 0])
            else:
                # Find least frequently used page
                i = 0
                min_freq = cache[0][1]
                for ii in range(1, len(cache)):
                    if cache[ii][1] < min_freq:
                        min_freq = cache[ii][1]
                        i = ii
                cache[i] = [e, 0]
        print("Cache:", cache)
    return counter / len(arr)


if __name__ == "__main__":
    pgSequence = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    frameSize = 3
    print("========== LFU ==========")
    hit_ratio = SeqLFU(pgSequence, frameSize)
    print("Hit Ratio:", hit_ratio)
