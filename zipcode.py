def format_zipcode(zip_code):
	if len(zip_code) <= 5:
		return '{:>05}'.format(zip_code)
	if len(zip_code) == 10:
		return str(zip_code)
	if len(zip_code) == 9:
		return '{}-{}'.format(zip_code[:5], zip_code[5:])
