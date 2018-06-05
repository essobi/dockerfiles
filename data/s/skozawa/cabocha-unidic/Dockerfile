FROM centos  
MAINTAINER Shunsuke Kozawa <shunsuke.kozawa@gmail.com>  
  
RUN yum install -y wget tar unzip gcc make gcc-c++ bzip2  
  
# MeCab  
RUN wget "https://mecab.googlecode.com/files/mecab-0.996.tar.gz" -O
mecab.tar.gz  
RUN tar -xzf mecab.tar.gz  
RUN cd mecab-0.996; ./configure --enable-utf8-only; make; make install;
ldconfig  
  
# MeCab-UniDic  
RUN wget
"http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Funidic%2F58338%2Funidic-
mecab-2.1.2_src.zip" -O unidic-mecab.zip  
RUN unzip unidic-mecab.zip  
RUN cd unidic-mecab-2.1.2_src; ./configure; make; make install  
# for using unidic as default dictionary  
RUN echo "dicdir = /usr/local/lib/mecab/dic/unidic" > /usr/local/etc/mecabrc  
  
# CRF++  
RUN wget "https://crfpp.googlecode.com/files/CRF%2B%2B-0.58.tar.gz" -O
CRF++.tar.gz  
RUN tar -xzf CRF++.tar.gz  
RUN cd CRF++-0.58; ./configure; make; make install  
  
# Cabocha  
RUN wget "https://cabocha.googlecode.com/files/cabocha-0.68.tar.bz2" -O
cabocha.tar.bz2  
RUN tar -xjf cabocha.tar.bz2  
RUN cd cabocha-0.68; ./configure --with-posset=unidic --with-charset=UTF8;
make; make install; ldconfig  
  
RUN rm -rf mecab.tar.gz mecab-0.996 unidic-mecab.zip unidic-mecab-2.1.2_src
CRF++.tar.gz CRF++-0.58 cabocha.tar.bz2 cabocha-0.68  

