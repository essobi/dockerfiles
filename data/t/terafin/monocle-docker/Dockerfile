FROM ubuntu:xenial  
  
VOLUME ["/config"]  
EXPOSE 5000  
RUN mkdir -p /usr/scanner  
RUN mkdir -p /config  
WORKDIR /usr/scanner  
RUN apt-get update --fix-missing  
RUN apt-get install --fix-missing -fy git python3.5 python3.5-dev python3-pip
libffi-dev libssl-dev mysql-client python3-cairo python3-pygeoif
python3-geopandas python3-gdal phantomjs chromium-browser curl  
RUN pip3 install --upgrade pip  
RUN pip3 install asyncpushbullet peony-twitter gpsoauth shapely selenium
uvloop psycopg2 aiosocks cchardet aiodns sanic asyncpg ujson monogen geos  
  
WORKDIR /usr/scanner  
  
RUN git clone \--recursive https://github.com/Noctem/Monocle.git
/usr/scanner/monocle  
RUN pip3 install -r /usr/scanner/monocle/requirements.txt  
RUN ln -s /config/config.py /usr/scanner/monocle/monocle/config.py  
RUN ln -s /config/accounts.csv /usr/scanner/monocle/accounts.csv  
  
COPY run.sh /usr/scanner/run.sh  
  
WORKDIR /usr/scanner/monocle  
  
RUN curl -sSL https://raw.githubusercontent.com/Imaginum/monocle-
icons/master/switch-icons.sh | bash  
RUN find . -name "*.py" -exec sed -i
"s/https:\/\/maps.google.com/https:\/\/maps.apple.com/g" {} \;  
  
CMD ["/usr/scanner/run.sh"]

