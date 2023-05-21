import glob
import csv
import matplotlib.pyplot as plt
files = glob.glob("./battle-results-csv/*.csv")
#ラインマーカーのブキ達
lmw = ["prime","jetsweeper","bucketslosher_deco"]
counts = []
for file in files:
    with open(file,mode="r",encoding="utf-8") as f:
        print("ーーー"+file+"ーーー")
        count = 0
        matchcount = 0
        reader = csv.reader(f)
        for row in reader:
            #row[21],を追加すれば投稿者も含む
            weapons = [row[29],row[37],row[45],row[53],row[61],row[69],row[77]]
            for weapon in weapons:
                if weapon in lmw:
                    count += 1
                    #print("ラインマーカーブキだった:"+weapon)
            matchcount += 1
        #この下のコメントアウトを消したら試合数に対する使用数を出す
        count = count / matchcount
        print(str(count))
        counts.append(count)
#x軸とx軸を設定（今回はリストを用いて表現します。）
X = range(len(counts))
Y = counts
#グラフプロット準備
plt.plot(X, Y)
#グラフ出力
plt.show()
