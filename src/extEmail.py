#######
# Given a string, extract the email address from string
# If there is no email address, print an appropriate error message
# Other specifications:
# - assume only string contains no more than one address
# - no special characters other than @ and . will be given
# - email address will be denoted between spaces
# - for example: hello a@b this@example.where this@.is.fun will print this@example.where
#######

# checks whether string is a valid email address
def is_valid_address(some_string):
    pos_at = some_string.find('@')
    pos_dot = some_string.find('.')
    if pos_at == -1 or pos_dot == -1:
        return False
    if pos_at > pos_dot:
        return False
    if abs(pos_at-pos_dot) == 1:
        return False
    if some_string.count('.') > 1 or some_string.count('@') > 1:
        return False
    if pos_at == 0 or pos_dot == len(some_string)-1:
        return False
    return True
 
          
# get user input
user_input = raw_input("Please enter a string: ")

# take care of simple case where can tell right away there is no email address
if '@' not in user_input:
    print "No valid email address found."
elif ' ' not in user_input:
    if is_valid_address(user_input):
        print "Address is:", user_input
    else:
        print "No valid email address found."
else:
    # case where user enters string with spaces
    at = 0
    # take care of case when valid address is the first string before any spaces
    start = 0
    end = user_input.find(' ', start+1)
    if is_valid_address(user_input[start:end]):
        print "Address is:",user_input[start:end]
    else:
        while True:
            start = user_input.find(' ', at)
            # start looking for the next space one index after the first space
            end = user_input.find(' ', start+1)
            # This part was left out of the video
            # Bug discovered later :)
            # handles case where email address has only one letter after dot
            # and is at the end of the user string
            if end == -1:
                if is_valid_address(user_input[start:]):
                    print "Address is:",user_input[start:]
                    break
            elif is_valid_address(user_input[start:end]):
                print "Address is:",user_input[start:end]
                break
            else:
                at = end
                # take care of case when valid email not found and
                # reached end of input string
                if at == -1:
                    print "No valid email address found."
                    break

