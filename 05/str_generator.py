def str_generator(file, filter_data):
    filter_lower = {x.lower() for x in filter_data}
    with open(file, 'r', encoding='utf-8') as f_data:
        for line in f_data:
            main = [x.lower().strip() for x in line.split(' ')]
            if len(set(main).intersection(filter_lower)) > 0:
                yield line.strip()
