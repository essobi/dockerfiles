FROM cariandrum22/rails-base  
  
MAINTAINER ikmy0709@gmail.com  
  
RUN apt-get install wget  
  
# install mecab  
RUN sudo wget https://mecab.googlecode.com/files/mecab-0.996.tar.gz && \  
tar -zxvf mecab-0.996.tar.gz && \  
cd mecab-0.996 && \  
./configure --enable-utf8-only && \  
make && \  
sudo make install && \  
cd ../ && \  
sudo ldconfig && \  
rm -rf mecab-0.996 && \  
sudo wget https://mecab.googlecode.com/files/mecab-
ipadic-2.7.0-20070801.tar.gz && \  
tar -zxvf mecab-ipadic-2.7.0-20070801.tar.gz && \  
cd mecab-ipadic-2.7.0-20070801 && \  
./configure --with-charset=utf8 && \  
make && \  
sudo make install && \  
cd ../ && \  
sudo ldconfig && \  
rm -rf mecab-ipadic-2.7.0-20070801  

