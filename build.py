import QieyunEncoder

純一等韻 = '冬模泰咍灰痕魂寒豪唐登侯覃談'
純二等韻 = '江佳皆夬刪山肴耕咸銜'
純三等韻 = '鍾支脂之微魚虞祭廢眞臻欣元文仙宵陽清蒸尤幽侵鹽嚴凡'
純四等韻 = '齊先蕭青添'

with open('廣韻(20170209).csv') as f, open('rhyme_book.csv', 'w') as g:
	next(f) # skip header

	print('資料名稱,小韻號,韻部原貌,最簡描述,反切覈校前,反切,字頭覈校前,字頭,釋義,釋義補充,圖片id', file=g)

	資料名稱 = '廣韻'

	for line in f:
		xs = line.rstrip('\n').split(',')
		反切覈校前, 反切, 字頭覈校前, 字頭, 釋義, 釋義補充, 母, 呼, 等, 韻, 聲, 韻部原貌, 圖片id, 小韻號 = xs[19], xs[20], xs[23], xs[24], xs[25], xs[26], xs[30], xs[31], xs[32], xs[33], xs[34], xs[39], xs[56], xs[58]

		小韻號 = int(小韻號)

		# 拆分重紐和韻
		重紐 = 韻[1:]
		韻 = 韻[:1]

		# 異體字
		if 母 == '群': 母 = '羣'
		elif 母 == '娘': 母 = '孃'

		if 韻 == '真': 韻 = '眞'

		# 刪除羨餘屬性
		if not (母 in '幫滂並明見溪羣疑影曉' and 韻 in '支脂祭眞仙宵清侵鹽'):
			重紐 = None
		if 母 in '幫滂並明' or 韻 in '東冬鍾江虞模尤幽':
			呼 = None

		# 邊緣小韻的等根據韻確定
		if 韻 in 純一等韻: 等 = '一'
		elif 韻 in 純二等韻: 等 = '二'
		elif 韻 in 純三等韻: 等 = '三'
		elif 韻 in 純四等韻: 等 = '四'

		# 無反切的小韻
		if len(反切覈校前) != 2: 反切覈校前 = ''
		if len(反切) != 2: 反切 = ''

		# patch
		if 反切 == '所庚': 等 = '三' # 據《切韻研究》改為三等。FIXME: 未來二、三等兼收，並加備註
		elif 反切 == '烏定': 呼 = '合' # 「鎣」小韻誤作開口，當為合口
		# 「間」「閒」「閑」改為後世正字。FIXME:「閑」作「閒」誤
		elif 反切 == '古閑' and 字頭 == '閒': 字頭 = '間'
		elif 反切 == '戶閒' and 字頭 == '閑': 字頭 = '閒'
		elif 反切 == '古莧' and 字頭 == '閒': 字頭 = '間'

		最簡描述 = QieyunEncoder.音韻地位(母, 呼, 等, 重紐, 韻, 聲).最簡描述

		if 反切覈校前 == 反切: 反切 = ''
		if 字頭覈校前 == 字頭: 字頭 = ''

		print(資料名稱, 小韻號, 韻部原貌, 最簡描述, 反切覈校前, 反切, 字頭覈校前, 字頭, 釋義, 釋義補充, 圖片id, sep=',', file=g)
