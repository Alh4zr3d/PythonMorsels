def sum_timestamps(tsLst):
    totalsec = 0
    for ts in tsLst:
        if len(ts.split(":")) == 3:
            hr,min,sec = ts.split(":")
            totalsec += int(sec) + int(min) * 60 + int(hr) * 3600
        else:
            min,sec = ts.split(":")
            totalsec += int(sec) + int(min) * 60
    if totalsec >= 3600:
        hours = str(totalsec//3600)
        remain = totalsec%3600
        return hours + ":" + str(remain//60).zfill(2) + ":" + str(totalsec%60).zfill(2)
    else:
        return str(totalsec//60) + ":" + str(totalsec%60).zfill(2)
