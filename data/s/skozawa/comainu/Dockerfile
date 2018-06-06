FROM ubuntu  
MAINTAINER Shunsuke Kozawa <shunsuke.kozawa@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential unzip wget && apt-get
clean  
  
# CRF++  
RUN wget --no-check-certificate
"https://crfpp.googlecode.com/files/CRF%2B%2B-0.58.tar.gz" -O CRF++.tar.gz  
RUN tar -xzf CRF++.tar.gz  
RUN cd CRF++-0.58; ./configure; make; make install  
  
# TinySVM  
RUN wget "http://chasen.org/~taku/software/TinySVM/src/TinySVM-0.09.tar.gz" -O
TinySVM.tar.gz  
RUN tar -xzf TinySVM.tar.gz  
RUN cd TinySVM-0.09; ./configure; make; make install;  
  
# Yamcha  
RUN wget "http://chasen.org/~taku/software/yamcha/src/yamcha-0.33.tar.gz" -O
yamcha.tar.gz  
RUN tar -xzf yamcha.tar.gz  
RUN wget --no-check-certificate
"https://gist.githubusercontent.com/skozawa/89024693963fd0adfa6d/raw/00ffa28de5ef11b902b4f35cbf3f3217bc62de3e/yamcha.patch"  
RUN patch -p0 < yamcha.patch; cd yamcha-0.33; ./configure; make; make install  
  
# MeCab  
RUN wget --no-check-certificate
"https://mecab.googlecode.com/files/mecab-0.996.tar.gz" -O mecab.tar.gz  
RUN tar -xzf mecab.tar.gz  
RUN cd mecab-0.996; ./configure --enable-utf8-only; make; make install;
ldconfig  
  
# MeCab-UniDic  
RUN wget
"http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Funidic%2F58338%2Funidic-
mecab-2.1.2_src.zip" -O unidic-mecab.zip  
RUN unzip unidic-mecab.zip  
RUN cd unidic-mecab-2.1.2_src; ./configure; make; make install  
  
# XXX Require Unidic2(XML) and SQLite3  
# Comainu  
RUN wget
"http://sourceforge.jp/frs/redir.php?m=iij&f=%2Fcomainu%2F60782%2FComainu-0.70-src.tgz"
-O Comainu-src.tgz  
RUN tar -xzf Comainu-src.tgz  
RUN wget
"http://sourceforge.jp/frs/redir.php?m=iij&f=%2Fcomainu%2F60782%2FComainu-0.70-model.tgz"
-O Comainu-model.tgz  
RUN tar -xzf Comainu-model.tgz  
RUN cd Comainu-0.70; ./configure  
  
RUN rm -rf CRF++.tar.gz CRF++-0.58 TinySVM.tar.gz TinySVM-0.09 yamcha.tar.gz
yamcha.patch yamcha-0.33 mecab.tar.gz mecab-0.996 unidic-mecab.zip unidic-
mecab-2.1.2_src Comainu-src.tgz Comainu-model.tgz  
  
ADD comainu /bin/comainu  
RUN chmod 755 /bin/comainu  

