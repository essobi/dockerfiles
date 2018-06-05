FROM django  
  
MAINTAINER budddddddha  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y apt-utils  
RUN apt-get install -y vim  
RUN apt-get install -y gcc  
RUN apt-get install -y wget  
RUN apt-get install -y libxslt-dev  
RUN apt-get install -y python-dev  
RUN apt-get install -y mecab  
RUN apt-get install -y libmecab-dev  
RUN apt-get install -y mecab-ipadic  
RUN apt-get install -y aptitude  
RUN aptitude install -y mecab-ipadic-utf8  
RUN apt-get install -y python-mecab  
RUN apt-get install -y build-essential  
RUN apt-get install -y openssl  
RUN apt-get install -y curl  
RUN apt-get install -y git  
  
# depoticaディレクトリ作成  
WORKDIR /home  
RUN mkdir depotica  
  
# dataディレクトリをコピー  
ADD data /home/depotica/data  
  
# pip(パッケージ)  
WORKDIR /home/depotica/data/buildfiles  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
RUN pip install --upgrade django-storages  
  
# mecabインストール  
WORKDIR /home/depotica/data/buildfiles/mecab-0.996  
RUN ./configure --enable-utf8-only  
RUN make  
RUN make install  
  
WORKDIR ~  
RUN echo -e 'include ld.so.conf.d/*.conf\n/usr/local/lib' > /etc/ld.so.conf  
RUN ldconfig  
  
# 辞書の登録  
## ipadicのインストール  
#WORKDIR /var/tmp  
#RUN curl -O https://mecab.googlecode.com/files/mecab-
ipadic-2.7.0-20070801.tar.gz  
#RUN tar zxfv mecab-ipadic-2.7.0-20070801.tar.gz  
RUN cp -R /home/depotica/data/buildfiles/mecab-ipadic-2.7.0-20070801
/var/tmp/mecab-ipadic-2.7.0-20070801  
WORKDIR /var/tmp/mecab-ipadic-2.7.0-20070801  
RUN ./configure --with-charset=utf8  
RUN make  
RUN make install  
  
WORKDIR /var/tmp  
RUN cp -R /home/depotica/data/buildfiles/mecab-python-0.996 /var/tmp/mecab-
python-0.996  
#RUN curl -O https://mecab.googlecode.com/files/mecab-python-0.996.tar.gz  
#RUN tar zxfv mecab-python-0.996.tar.gz  
WORKDIR /var/tmp/mecab-python-0.996  
RUN rm setup.py  
RUN cp /home/depotica/data/buildfiles/mecab-python-0.996/setup.py .  
# ADD /home/ec2-user/depotica/data/mecab/mecab-python-0.996/setup.py
./setup.py  
WORKDIR /var/tmp  
# ADD /data/mecab/Station-Line-2015-04-15.csv ./Station-Line-2015-04-15.csv  
RUN cp /home/depotica/data/buildfiles/Station-Line-2015-04-15.csv .  
RUN /usr/local/libexec/mecab/mecab-dict-index -d
/usr/local/lib/mecab/dic/ipadic -u station-line.dic -f utf-8 -t utf-8 Station-
Line-2015-04-15.csv  
  
RUN rm /usr/local/lib/python3.4/site-packages/storages/backends/s3boto.py  
RUN cp /home/depotica/data/buildfiles/s3boto.py /usr/local/lib/python3.4/site-
packages/storages/backends/s3boto.py  
  
#VOLUME  
EXPOSE 80 5432  
WORKDIR /home/depotica  
  
#ENTRYPOINT ["/home/depotica/src/"]  
#CMD ["python", "manage.py", "runserver", "[::]:80"]  

