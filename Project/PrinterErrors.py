def printer_error(s):
    return str(len(list((x for x in s if ord(x) > ord('m'))))) + "/" + str(len(s))
