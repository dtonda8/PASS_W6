from data_structures.linked_stack import LinkedStack

def max_nesting(s: str) -> int:
	open_brk_st = LinkedStack()

	current_nesting = 0
	max_nesting = 0
	for ch in s:
		if ch == "(":
			open_brk_st.push(ch)
			current_nesting += 1
			max_nesting = max(max_nesting, current_nesting)
		elif ch == ")":
			current_nesting -= 1
			open_brk_st.pop()

	return max_nesting

if __name__ == "__main__": 
	pass