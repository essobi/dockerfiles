FROM postgres:alpine  
  
MAINTAINER Jack A Ross <jack.ross@technekes.com>  
  
RUN set -ex \  
\  
&& apk add --update --no-cache --virtual .fetch-deps \  
ca-certificates \  
openssl \  
unzip \  
wget \  
git \  
\  
&& apk add --update --no-cache --virtual .run_deps \  
freetds \  
python \  
\  
&& apk add --update --no-cache --virtual .build-deps \  
freetds-dev \  
gcc \  
libc-dev \  
make \  
python-dev \  
py-pip \  
\  
&& pip install --upgrade pip\  
\  
&& apk add --update --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/main/ --virtual .build-deps \  
postgresql-dev \  
\  
&& rm -rf /usr/local/include \  
&& ln -s /usr/include/ /usr/local/include \  
\  
&& cd /tmp \  
&& wget -O "tds_fdw.zip"
"https://github.com/GeoffMontee/tds_fdw/archive/master.zip" \  
&& unzip tds_fdw.zip \  
&& cd tds_fdw-master \  
\  
&& make USE_PGXS=1 \  
&& make USE_PGXS=1 install \  
\  
&& cd /tmp \  
&& git clone git://github.com/Kozea/Multicorn.git \  
&& cd Multicorn \  
&& make && make install \  
\  
&& cd /tmp \  
&& git clone git://github.com/lincolnturner/gspreadsheet_fdw.git \  
&& cd gspreadsheet_fdw \  
&& pip install --upgrade oauth2client gspread\  
&& python setup.py install \  
# \  
# && cd /tmp \  
# && pip install --upgrade sqlalchemy\  
# && pip install --upgrade git+https://github.com/pymssql/pymssql.git\  
\  
&& apk del \  
.fetch-deps \  
.build-deps \  
\  
&& rm -rf /tmp/tds_fdw* \  
&& rm -rf /tmp/Multicorn \  
&& rm -rf /tmp/gspreadsheet_fdw  
  
COPY ./docker-entrypoint-extended.sh /docker-entrypoint-extended.sh  
  
ENTRYPOINT ["/docker-entrypoint-extended.sh"]  
  
# don't know why we need this, but the base image CMD is not getting inherited  
CMD ["postgres"]  

