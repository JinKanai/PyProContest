class IrohaniGenerator:

    def __init__(self):
        self.irohanibun = set()
        self.irohani_dict = {'sakubun_list': []}
        self._generate_irohani_bun()

    def _generate_irohani_bun(self):
        import random
        while len(self.irohanibun) < 47:
            target = random.randrange(0x3042, 0x3093)
            if self._can_listed(target):
                self.irohanibun.add(chr(target))

    def _can_listed(self, target):
        import jaconv
        ignore_list = [0x3043, 0x3045, 0x3047, 0x3049,
                       0x3063, 0x3083, 0x3085, 0x3087, 0x308e]
        katakana = jaconv.hira2hkata(chr(target))
        r = True if len(katakana) == 1 and target not in ignore_list else False
        return r


def _main():
    iroha = IrohaniGenerator()
    for i, kana in enumerate(iroha.irohanibun, start=1):
        print(kana, end='')
        if i % 5 == 0:
            print('')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(_main())
