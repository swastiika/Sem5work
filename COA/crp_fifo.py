def SeqFIFO(arr, fsize):
    queue = []
    counter = 0
    for i in arr:
        if i in queue:
            counter += 1  # Hit
        else:
            if len(queue) >= fsize:
                queue.pop(0)  # Remove oldest page
            queue.append(i)
        print("Cache:", queue)
    return counter / len(arr)

    

if __name__ == "__main__":
    pgSequence = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    frameSize = 3
    print("========== FIFO ==========")
    hit_ratio = SeqFIFO(pgSequence, frameSize)
    print("Hit Ratio:", hit_ratio)
