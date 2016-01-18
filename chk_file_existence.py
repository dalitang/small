try:
	filename
excpet NameError:
	filename = 'what you like.'

# alternative

if not 'filename' in locals() or 'filename' in globals():
	filename = 'what you like.'
