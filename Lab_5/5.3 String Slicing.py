# 5.3 Simple indexing and Slicing implementation
# Define a string
text = "Python Programming"

# Indexing
print("First character:", text[0])    # P
print("Last character:", text[-1])    # g

# Slicing
print("First 6 characters:", text[0:6])   # Python
print("Characters from index 7 to 12:", text[7:13]) # Progra (manual says Progra, wait text[7:13] is 'rogra' if 0-based. 'Python ' is 0-6 (7 chars). P0 y1 t2 h3 o4 n5 [space]6 P7. So 7 is P. 13 is m. P r o g r a. Yes.)
print("Every second character:", text[::2]) # Pto rgamn (P t o [space] r g a m n).
print("Reversed string:", text[::-1])   # gnimmargorP nohtyP
