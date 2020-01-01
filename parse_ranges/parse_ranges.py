def parse_ranges(rangeStr):
    rngs = rangeStr.split(",")
    for rng in rngs:
        rnglst = rng.strip().split("-")
        if len(rnglst) == 2:
            start,end = rnglst
            if ">" in end:
                end = start
        else:
            start = end = rnglst[0]
        for x in range(int(start),int(end)+1):
            yield x        
