def read_file(filename):
	lines = []
	with open(filename, "r", encoding="utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines
def convert(lines):
	Allen_word_count = 0
	Allen_sticker_count = 0
	Allen_image_count = 0
	Viki_word_count = 0
	Viki_sticker_count = 0
	Viki_image_count = 0
	for line in lines:
		s= line.split(" ")
		name = s[1]
		time = s[0]
		if name =="Allen":
			if s[2] == "貼圖":
				Allen_sticker_count += 1
			elif s[2] == "圖片":
				Allen_image_count += 1
			else:
				for m in s[2:]:
					Allen_word_count += len(m)
		if name == "Viki":
			if s[2] == "貼圖":
				Viki_sticker_count += 1

			elif s[2] == "圖片":
				Viki_image_count += 1

			else:
				for m in s[2:]:
					Viki_word_count += len(m)
	print("Allen總共說了", Allen_word_count , "字")
	print("Allen總共傳了",Allen_sticker_count , "個貼圖")
	print("Allen總共傳了",Allen_image_count , "個圖片")
	print("Viki總共說了", Viki_word_count , "字")
	print("Viki總共傳了",Viki_sticker_count , "個貼圖")
	print("Viki總共傳了",Viki_image_count , "個圖片")
	

def write_file(filename,lines):
	with open(filename, "w", encoding="utf-8-sig") as f:
		for line in lines:
			f.write(line + "\n")


def main():
	lines = read_file("LINE-Viki.txt")
	lines = convert(lines)
	# write_file("nnn.txt",lines)

main()