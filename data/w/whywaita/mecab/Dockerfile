FROM ubuntu:latest  
  
RUN apt update -qq ;\  
apt install -y wget build-essential  
  
# Mecab  
RUN wget -O mecab-0.996.tar.gz
"https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE"
;\  
tar -xzf mecab-0.996.tar.gz ;\  
cd mecab-0.996; ./configure --enable-utf8-only; make; make install; ldconfig  
  
# Ipadic  
RUN wget -O mecab-ipadic-2.7.0-20070801.tar.gz
"https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
;\  
tar -xzf mecab-ipadic-2.7.0-20070801.tar.gz ;\  
cd mecab-ipadic-2.7.0-20070801; ./configure --with-charset=utf8; make; make
install ;\  
echo "dicdir = /usr/local/lib/mecab/dic/ipadic" > /usr/local/etc/mecabrc  
  
# Clean up  
RUN apt remove -y build-essential ;\  
rm -rf rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* ;\  
rm -rf mecab-0.996.tar.gz* ;\  
rm -rf mecab-ipadic-2.7.0-20070801*  

