def insert_demo(s, ch, k):
    # insert ch at kth index of s
    modified_string = s[:k]+ ch + s[k:]
    print("modified string:", modified_string)
    
if __name__ == "__main__":
    original_string = "GeeksforGeeks"
    ch_to_insert  = "for"
    index = 5
    
    print("original string:", original_string,)
    insert_demo(original_string, ch_to_insert, index)
    
    