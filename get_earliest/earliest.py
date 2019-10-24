def get_earliest(*dates):
    date_list = []
    for date in dates:
        date = date.split("/")
        date_list.append(date)
    zip_list = list(zip(*date_list))
    min_yr = min(zip_list[2])
    yrs = []
    for date in date_list:
        if min_yr in date:
            yrs.append(date)
    if len(yrs) == 1:
        return '/'.join(yrs[0])
    else:
        zip_months = list(zip(*yrs))
        min_mo = min(zip_months[0])
        mos = []
        for date in date_list:
            if min_mo in date:
                mos.append(date)
        if len(mos) == 1:
            return '/'.join(yrs[0])
        else:
            zip_days = list(zip(*mos))
            min_day = min(zip_days[1])
            days = []
            for date in date_list:
                if min_day in date:
                    return '/'.join(date)
            
        
    
