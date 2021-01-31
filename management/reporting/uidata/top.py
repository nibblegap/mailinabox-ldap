def select_top(c, select, start, end, y, fields, field_types):
    '''`c` is a cursor

    `select` is the select query `start` and `end` are the range in
the format YYYY-MM-DD HH:MM:SS and the select query must have
substitutes 'start_date' and 'end_date'.

    `y` is a description of the dataset

    `fields` are all fields to select by name

    `field_types` are the corresponding field types the caller will
    need to render the data visuals
    '''
    
    top = {
        'start': start,
        'end': end,
        'y': y,
        'fields': fields,
        'field_types': field_types,
        'items': []
    }
    for row in c.execute(select, {
            'start_date':start,
            'end_date':end
    }):
        v = {}
        for key in fields:
            v[key] = row[key]            
        top['items'].append(v)
    return top
