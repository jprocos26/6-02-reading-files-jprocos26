# problems

def toString(fileName):
    # This function returns the text from a given file.
    # Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    f.close()
    return out


def longestLine(fileName):
    # Given a file return the longest line from within that file
    f = open(fileName)
    longest = ""
    
    for line in f:
        line = line.strip()
        if len(line) > len(longest):
            longest = line
    
    f.close()
    return longest


def toBinary(fileName):
    # Given a file that is only 0's and 1's return a list of the file broken into bytes.
    # An example return might be ['01101001', '00101010', '1010']
    f = open(fileName)
    text = f.read()
    f.close()
    
    # Remove any spaces or newlines
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    
    # Break into chunks of 8
    bytes_list = []
    i = 0
    
    while i < len(text):
        byte = ""
        for j in range(8):
            if i < len(text):
                byte = byte + text[i]
                i = i + 1
            else:
                break
        bytes_list.append(byte)
    
    return bytes_list


# tests

print("creating test files")

#  ExampleText
file1 = open("ExampleText.txt", "w")
file1.write("Here is the text\ni am another line")
file1.close()

#  longest line test
file2 = open("LongestLineTest.txt", "w")
file2.write("short\n")
file2.write("this is a much longer line\n")
file2.write("medium line\n")
file2.close()

#  binary test
file3 = open("BinaryTest.txt", "w")
file3.write("011010010010101010101010")
file3.close()

print("test files created")

# Test 1: toString
print("Test 1, toString")
result = toString("ExampleText.txt")
print(f"Result: {repr(result)}")
print(f"Expected: 'Here is the text\\ni am another line'")
print(f"Pass: {result == 'Here is the text\\ni am another line'}\n")

# Test 2: longestLine
print("Test 2, longestLine")
result = longestLine("LongestLineTest.txt")
print(f"Result: '{result}'")
print(f"Expected: 'this is a much longer line'")
print(f"Pass: {result == 'this is a much longer line'}\n")

# Test 3: toBinary
print("Test 3, toBinary")
result = toBinary("BinaryTest.txt")
print(f"Result: {result}")
print(f"Expected: ['01101001', '00101010', '10101010']")
print(f"pass: {result == ['01101001', '00101010', '10101010']}\n")

print("all tests done")
