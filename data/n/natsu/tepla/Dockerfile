from ubuntu:14.04  
maintainer natsu  
  
run apt-get update  
run apt-get install -y gcc wget git xz-utils m4 build-essential --no-install-
recommends  
  
# openssl install  
workdir /tmp  
run wget http://www.openssl.org/source/openssl-1.0.2d.tar.gz && \  
tar xvfz openssl-1.0.2d.tar.gz  
workdir openssl-1.0.2d  
run ./config --prefix=/usr/local shared && \  
make && \  
make test && \  
make install  
  
# gmp install  
workdir /tmp  
run wget --no-check-certificate
https://gmplib.org/download/gmp/gmp-6.0.0a.tar.xz && \  
tar Jxvf gmp-6.0.0a.tar.xz  
workdir gmp-6.0.0/  
run ./configure --prefix=/usr/local \--enable-cxx && \  
make && \  
make check && \  
make install  
  
# tepla install  
workdir /tmp  
run wget http://www.cipher.risk.tsukuba.ac.jp/tepla/download/tepla-1.0.tar.gz
&& \  
tar zxvf tepla-1.0.tar.gz  
workdir tepla-1.0  
run ./configure && \  
make && \  
make check && \  
make install  
  
workdir /  
run rm -rf /tmp/*  
# キャッシュの削除(イメージの容量削減)  
run apt-get upgrade -y && apt-get clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  
  
# サンプルファイルの追加  
add sample /root/sample  

