FROM ubuntu:latest  
MAINTAINER kvvzr kwzr@twinkrun.net  
  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
unzip \  
python \  
python-pip \  
python-dev \  
sqlite3 \  
timidity \  
freepats \  
lame \  
mecab \  
libmecab-dev \  
python-mecab \  
python-mysqldb  
  
ENV TWITTER_API_KEY xxx  
ENV TWITTER_API_SECRET xxx  
  
RUN wget -O unidic.zip
"http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Funidic%2F58338%2Funidic-
mecab_kana-accent-2.1.2_src.zip" && unzip unidic.zip  
RUN cd unidic-mecab_kana-accent-2.1.2_src && ./configure --disable-debug
--disable-dependency-tracking && make install  
RUN echo "dicdir = /usr/lib/mecab/dic/unidic" > /etc/mecabrc  
RUN git clone \--depth 1 https://github.com/kvvzr/Melete.git  
RUN cd Melete && pip install -r requirements.txt && \  
python app.py db init && \  
python app.py db migrate && \  
python app.py db upgrade && \  
python app.py seed  
  
EXPOSE 8000  
WORKDIR /Melete  
ENTRYPOINT ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "--reload",
"app:app"]  

