def SeqLRU(seq, fsize):
    cache = []  # List of [page, age]
    counter = 0
    for e in seq:
        pages = [x[0] for x in cache]
        if e in pages:
            for k in cache:
                if k[0] == e:
                    k[1] = 0  # Reset age
            counter += 1  # Hit
        else:
            # Increase age of all pages
            cache = [[k[0], k[1] + 1] for k in cache]
            if len(cache) < fsize:
                cache.append([e, 0])
            else:
                # Evict the oldest (highest age)
                oldest_index = 0
                max_age = cache[0][1]
                for ii in range(1, len(cache)):
                    if cache[ii][1] > max_age:
                        max_age = cache[ii][1]
                        oldest_index = ii
                cache[oldest_index] = [e, 0]
        print("Cache:", cache)
    return counter / len(seq)

    

if __name__ == "__main__":
    pgSequence = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    frameSize = 3
    print("========== LRU ==========")
    hit_ratio = SeqLRU(pgSequence, frameSize)
    print("Hit Ratio:", hit_ratio)
