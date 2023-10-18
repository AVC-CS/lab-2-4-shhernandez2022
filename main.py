def main():

    original_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################

    secondP = original_str.find('p' , 1)
    sub2 = original_str[secondP:]
    sub1 = original_str[:secondP-1]
    merged_str = sub2 + ' ' + sub1

    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
