FROM mysql:5.7  
  
RUN apt-get update && apt-get install -yq mecab libmecab-dev unzip curl g++
make && \  
curl -sSL -o /tmp/mecab-ko.tar.gz https://bitbucket.org/eunjeon/mecab-ko-
dic/downloads/mecab-ko-dic-2.0.1-20150920.tar.gz && \  
cd /tmp/ && tar xvzf mecab-ko.tar.gz && cd mecab-ko-dic-2.0.1-20150920 && \  
./configure && make && make install && \  
echo "dicdir=/usr/lib/mecab/dic/mecab-ko-dic" > /etc/mecabrc && \  
echo "plugin-load=mecab=libpluginmecab.so" >> /etc/mysql/my.cnf && \  
echo "loose-mecab-rc-file=/etc/mecabrc" >> /etc/mysql/my.cnf && \  
echo "innodb_ft_min_token_size=1" >> /etc/mysql/my.cnf  

