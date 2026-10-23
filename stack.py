stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek
print("Top element:", stack[-1])

# Pop
item = stack.pop()
print("Deleted element:", item)

print("Stack after pop:", stack)

# Check empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")