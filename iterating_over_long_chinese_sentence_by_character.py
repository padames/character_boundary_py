#!/usr/bin/env python3

def main():
    #  from https://stackoverflow.com/q/1738788/1585486
    s = u"简讯：新華社報道，美國總統奧巴馬乘坐的「空軍一號」專機晚上10時42分進入上海空域，預計約30分鐘後抵達浦東國際機場，開展他上任後首次訪華之旅。"
    [print(c) for c in s]

if __name__ =="__main__":
    main()