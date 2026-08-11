with open("iisers/iisertvm.html", "r+") as f:
	contents = f.read().replace("**", "<strong>")
	f.write(contents)
	print(contents)
print("changed successfully")