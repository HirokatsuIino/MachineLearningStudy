# using
# pip install stanfordnlp
# python text.py
# https://dev.classmethod.jp/articles/python-stanford-nlp/

#-*- coding:utf-8 -*-
import stanfordnlp

# stanfordnlp.download('ja') # モデルのダウンロード(一回実行すれば、以降は不要)

# lang(仕様言語)とtreebank(ツリーバンク=コーパスの一種)を指定
nlp = stanfordnlp.Pipeline(lang="ja", treebank="ja_gsd")
# doc = nlp("今日も、晴れでした。いい天気でした。")
doc = nlp("３０年以上にわたる不動産業の実績。ビジネスモデル特許。ＳＢＩホールディングスとの資本業務提携による不動産とＩＴの融合。")
# doc = nlp("女子大生を中心とした産学連携型アイディアソンのプラットフォーム事業")
# doc = nlp("昨日の夜、私は大学時代の友人と食事に行きました。")
doc.sentences[0].print_dependencies()

print('----------')

words = doc.sentences[0].words
word = ''

for w in words:
    word += w.text + ' '

print(word)
