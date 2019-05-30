
class SekainoNabeatsu:
    """
    与えられた数までのナベアツ数をリストで返す
    """

    def __init__(self, upper_limit):
        self.places = ['','ジュウ','ヒャク','セン','マン']
        self.numbers = ['','イチ','ニ','サ～ン','ヨン','ゴ','ロク','ナナ','ハチ','キュウ']
        self.upper_limit = upper_limit + 1
        self.nabeatsu_number = []
        self._main_loop()

    def _main_loop(self):
        for i in range(1,self.upper_limit):
            n=i
            if i%3 == 0 or '3' in str(i):
                n=self._make_nabeatsu(i)
            self.nabeatsu_number.append(n)

    def _make_nabeatsu(self,org_num):
        result = ''
        str_num = str(org_num)
        digits = len(str_num)
        for i,num in enumerate(str_num):
            current_place = (digits-i)-1
            if current_place == 0 or num != '1' and digits != 1:
                result += self.numbers[int(num)]
            result += self.places[current_place]
        return(self._ahonize(result))

    def _ahonize(self,nabeatsu_number):
        r = nabeatsu_number + '！！'
        if 'サ～ン！！' not in r:
            p  = len(nabeatsu_number) -1
            r = nabeatsu_number[:p] + '～' + nabeatsu_number[p:] + '！！'
        return r

def main():
    sekaino = SekainoNabeatsu(1000)
    for i in sekaino.nabeatsu_number:
        print(i)

if __name__ == '__main__':
    main()
