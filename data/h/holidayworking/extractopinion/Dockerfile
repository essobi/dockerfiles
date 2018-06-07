FROM perl:5.10.1  
MAINTAINER Hidekazu Tanaka <hidekazu.tanaka@gmail.com>  
  
RUN apt-get update && apt-get install -y locales --no-install-recommends && rm
-rf /var/lib/apt/lists/* && \  
echo ja_JP.UTF-8 UTF-8 > /etc/locale.gen && \  
locale-gen && \  
update-locale LANG=ja_JP.UTF-8  
  
RUN apt-get update && apt-get install -y gawk --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN cpanm Text::CSV_XS  
  
COPY patch/crf.patch /tmp/crf.patch  
RUN curl -SL
https://858ca1c29e475f0e4e56bfc9b1de8778db1cc6a8.googledrive.com/host/0B4y35FiV1wh7fngteFhHQUN2Y1B5eUJBNHZUemJYQV9VWlBUb3JlX0xBdWVZTWtSbVBneU0/CRF++-0.54.tar.gz
| tar -xzC /usr/local/src && \  
cd /usr/local/src/CRF++-0.54 && \  
patch -u < /tmp/crf.patch && ./configure && make && make install && ldconfig
&& \  
rm -rf /usr/local/src/CRF++-0.54  
  
RUN curl -SL http://nlp.ist.i.kyoto-u.ac.jp/nl-
resource/juman/juman-6.01.tar.gz | tar -xzC /usr/local/src && \  
cd /usr/local/src/juman-6.01 && \  
./configure && make && make install && ldconfig && \  
rm -rf /usr/local/src/juman-6.01  
  
RUN curl -SL http://www.corpit.ru/mjt/tinycdb/tinycdb-0.78.tar.gz | tar -xzC
/usr/local/src && \  
cd /usr/local/src/tinycdb-0.78 && \  
make && make install && ldconfig && \  
rm -rf /usr/local/src/tinycdb-0.78  
  
RUN curl -SL http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-3.01.tar.gz |
tar -xzC /usr/local/src && \  
cd /usr/local/src/knp-3.01 && \  
./configure && make && make install && ldconfig && \  
rm -rf /usr/local/src/knp-3.01  
  
RUN curl -SL https://alaginrc.nict.go.jp/opinion/src/extractopinion-1.2.tar.gz
| tar -xzC /opt && \  
cd /opt/extractopinion-1.2 && \  
cd svmtools && make clean && make && \  
cd ../pol && make clean && make  
  
CMD /opt/extractopinion-1.2/extract.sh /opt/extractopinion-1.2/sample.txt  

