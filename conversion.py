
#method for the dollar to phonetic conversion
def toCheck(string):
    #translation for the one's and hundred's place
    translations = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
                    "8": "eight", "9": "nine", "0": ""}
    #translation for the ten's place
    tens_place = {"1": "ten", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy",
                    "8": "eighty", "9": "ninety", "0": ""}
    #translation for when there is a 1 in the tens place
    one_tens = {"1": "eleven", "2": "twelve", "3": "thirteen", "4": "fourteen", "5": "fifteen", "6": "sixteen",
                "7": "seventeen", "8": "eighteen", "9": "nineteen", "0": "ten"}
    #translation for the extension
    place = {0: "", 1: "thousand", 2: "million", 3: "billion", 4: "trillion"}
    place_counter = 0

    to_return = ""
    change = ""
    #get rid of dollar sign
    string = string.replace("$", "")

    #check for any change
    if "." in string:
        change = "and " + string[string.index(".") + 1:] + "/100 "
        string = string[:string.index(".")]

    #split the string on the commas to form a list of strings
    string_arr = string.split(",")

    #loop through each string within the list
    for bucket in string_arr[::-1]:
        to_add = ""
        #handle length of 3
        if len(bucket) == 3:
            if bucket[0] != "0":
                to_add += translations[bucket[0]] + " hundred "
            #check if the tens place contains a 1
            if bucket[1] == "1":
                to_add += one_tens[bucket[2]]
            else:
                #check is their needs to be a dash or not
                if bucket[2] != "0" and bucket[1] != "0":
                    to_add += tens_place[bucket[1]] + "-" + translations[bucket[2]]
                else:
                    to_add += tens_place[bucket[1]] + translations[bucket[2]]
        #handle length of 2
        elif len(bucket) == 2:
            #check if the tens place contains a 1
            if bucket[0] == "1":
                to_add += one_tens[bucket[1]]
            else:
                #check if there needs to be a dash or not
                if bucket[1] != "0":
                    to_add += tens_place[bucket[0]] + "-" + translations[bucket[1]]
                else:
                    to_add += tens_place[bucket[0]] + translations[bucket[1]]
        #handle length of 1
        elif len(bucket) == 1:
            to_add += translations[bucket[0]]

        #add the extension to the value
        to_add += " " + place[place_counter] + " "

        place_counter += 1
        to_return = to_add + to_return

    #add on the change and dollars
    to_return = to_return[:-1] + change + "dollars"

    return to_return

def main():
    print("The phonetic representation is: " + toCheck(input("Please enter a dollar amount: ")))

if __name__ == '__main__':
    main()
