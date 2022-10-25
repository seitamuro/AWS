# 概要

AWS CloudFormation内で使えるパッケージを作成してみる

パッケージの内容としては指定されたURLの内容を指定したS3にアップロードするというもの。

# メモ

- マクロの実体はLambda
- LambdaのARNを`AWS::CloudFormation::Macro`リソースに指定することでスタック作成時に関数実行
- そうするとLambdaにペイロードが渡される

# 参考文献

https://qiita.com/umi/items/400b730cf72f6cf1e2a1