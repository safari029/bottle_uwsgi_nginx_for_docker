# bottle_uwsgi_nginx_for_docker

# 概要
pythonのWEBフレームワーク(Bottle)で作ったファイルをdocker上で動かすサンプル

# Usage
```
# Dockerfileと必要なファイル類をclone
git clone https://github.com/safari029/bottle_uwsgi_nginx_for_docker/

# imageを作成
docker build -t test_image .

# dockerのimageが作成されていることを確認
docker images

# test という名前でrun
docker run -it -p 80:80 --name test test_image

# docker 起動確認
docker ps

# web動作確認
$ curl localhost
Hello World!

# docker rm
rm -f test
```

# Reference
https://github.com/tiangolo/uwsgi-nginx-docker
