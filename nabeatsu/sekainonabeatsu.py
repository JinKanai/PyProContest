class SekainoNabeatsu:
    """

    世界のナベアツ数を返すクラス

    Parameters
    ----------
    stop_number : int
        ナベアツ数を得たい上限数

    Returns
    -------
    list
         通常数とナベアツ数のリスト
    """

    def __init__(self, stop_number, start_number):
        self.start_number = start_number
        self.stop_number = stop_number
        self.places = ['', 'ジュウ', 'ヒャク', 'セン', 'マン', 'ジュウ','ヒャク', 'セン', 'オク']

        # ３は必ずアホになるのであらかじめ～を付けとく
        self.numbers = ['', 'イチ', 'ニ', 'サ～ン',
                        'ヨン', 'ゴ', 'ロク', 'ナナ', 'ハチ', 'キュウ']
        self.nabeatsu_number = []
        self._main_loop()

    def _main_loop(self):
        for i in range(self.start_number, self.stop_number + 1):
            n = i
            if i % 3 == 0 or '3' in str(i):
                n = self._make_nabeatsu(i)
            self.nabeatsu_number.append(n)

    def _make_nabeatsu(self, org_num):
        """
        渡された数からナベアツ数を抽出
        > ナベアツ数・・・アホになる数のこと
        """
        result = ''
        str_num = str(org_num)

        # 桁数を出しとく
        digits = len(str_num)

        for i, num in enumerate(str_num):
            # 今処理している桁
            current_place = (digits - i) - 1

            # イチヒャク、イチセンとかいう記載にならないようにする判定if文
            # 取り出してる数字が１でなくかつ2桁以上の数字のときのみナベアツ数に変換
            # ただし処理している桁が1の位の時はナベアツ数に変換
            if current_place == 0 or num != '1' and digits != 1:
                result += self.numbers[int(num)]
            result += self.places[current_place]
        return (self._ahonize(result))

    def _ahonize(self, nabeatsu_number):
        """
        ナベアツ数をアホ化する処理
        """

        # 先に末尾に！！を付けて、次のif文で一の位を見つけやすくする
        r = nabeatsu_number + '！！'

        # 1の位のサ～ンに二重で～が付かないようにする判定if文
        if 'サ～ン！！' not in r:
            p = len(nabeatsu_number) - 1
            # 1の位以外のナベアツ数をアホにするために、最後の1文字目の前に～を挿入。
            # ！！が入っていると場所がうまく取れないため、！！を付ける前の引数を利用
            r = nabeatsu_number[:p] + '～' + nabeatsu_number[p:] + '！！'
        return r


def _main():
    import argparse
    parser = argparse.ArgumentParser(description="世界のナベアツ")
    parser.add_argument("count", type=int, help="ナベアツ上限数（１０万まで対応）")
    parser.add_argument("--start", type=int, help="開始する数")
    args = parser.parse_args()

    start_number = 1
    if args.start:
        start_number = args.start

    # 実行したい数をSekainoNabeatuクラスに渡してインスタンス化
    sekaino = SekainoNabeatsu(args.count, start_number )

    for i in sekaino.nabeatsu_number:
        print(i)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(_main())
