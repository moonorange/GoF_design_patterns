# 8 Abstact Factory
抽象的な部品を組み合わせて抽象的な製品を作る


# 実装

## 抽象的な部品

### Item
linkとtrayのスーパークラス
linkとtrayを同一視するためのクラス
caption fieldはこの項目の見出し
makehtml methodは抽象メソッドでhtmlの文字列が返り値となるようサブクラスで実装

### Link
htmlのハイパーリンクを抽象的に表現したクラス
url fieldはリンクの飛び先url
makehtmlを実装してないので抽象クラス

### Tray
複数のlinkやtrayを集めてひとまとまりにしたもの
linkやtrayをadd methodで集める。それらのsuper classであるitemを引数にとる
makehtmlを実装してないので抽象クラス

## 抽象的な製品

### Page
htmlページ全体を抽象的に表現したクラス
linkやtrayが抽象的な部品であるならpageは抽象的な製品
title　fieldはページのタイトル
authorはページの作者
add methodでitemを追加する
output methodでタイトルを元にファイル名を決定しmakeHTML methodで内容をファイルに書き込む
makeHTMlを抽象メソッドとして定義

### 抽象的な工場

### Factory
get_factory methodはクラス名を指定して具体的な工場のインスタンスを生成するもの。ただし戻り値は抽象的な工場
create_link, tray, pageの各メソッドは抽象的な工場で部品や製品を作るときに用いるメソッド
具体的な作成はサブクラスだがシグニチャ(引数の型と数)とメソッドの名前は決められている

## 具体的な工場

### ListFactory
create_link, tray, pageを実装

## 具体的な部品

### ListLink
linkのサブクラス
make_htmlを実装

### ListTray
trayのサブクラス
make_htmlを実装。tray fieldの中のitemをhtmlのタグとして表現する

## 具体的な製品

### ListPage
Pageのサブクラス
make_html methodを実装


# 登場人物

## AbstractProduct
抽象的な部品や製品のinterface

## AbstractFactory
AbstractProductのインスタンスを作り出すためのインターフェース

## Client
AbstractFactoryとAbstractProductのインターフェースだけを使って仕事を行う役

## CreateProduct
AbstractProductのインターフェースの実装をする

## ConcreteFactory
AbstractFactoryのインターフェースを実装

#　知っておくべきこと

## 具体的な工場を新たに追加するのは簡単
いくら具体的な工場を追加しても抽象的な工場やmain関数に修正を加える必要はない

## 部品を新たに追加するのは困難
AbstarctFactoryに新たな部品を追加しようとすると具体的な工場全てに修正加えなければならない
