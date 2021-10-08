class Nihongo:
    def eng_jpn(self, number):
        jpnfw = ["一", "二","三", "四", "五", "六","七","八","九","十", "二十", "三十", "四十", "五十", "六十", "七十", "八十", "九十","百","千","万", "十万","百万","千万","一億", "十億", "百億", "兆"]
        engfw = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,1000,10000,100000,1000000, 10000000, 100000000, 1000000000,10000000000,1000000000000]
        jpn = jpnfw[::-1]
        eng = engfw[::-1]
        self.number = number
        japanese = ''
        count = 0
        while number>0:
            for x in range(number // eng[count]):
                japanese += jpn[count]
                number -= eng[count]
            count+=1
      
        for character in japanese:
            count_char = japanese.count(character)
            if count_char > 1:

                replace_with = jpn[-count_char]
                print(replace_with, ":", character)
                japanese = japanese.replace(character*(count_char),replace_with + character)
        return(japanese)
print(Nihongo().eng_jpn(2065))