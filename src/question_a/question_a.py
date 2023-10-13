#write functions here, don't add input('') statements here!

def test_config():
    return True

def reverse_string(string1):
    reverse_string = ""
    count = len(string1)

    while count > 0:
        reverse_string += string1[count - 1]
        count = count -1 
    return reverse_string
