from zomato_lookup import Zomato_Lookup

if __name__ == "__main__":
	a = Zomato_Lookup(raw_input())# in place of raw_input u give ur restaurant name like eg : 'paradise restaurant hyderabad' or 'hazzel ice cream hyderabad'
	                                 #format is name place
	print a.url

