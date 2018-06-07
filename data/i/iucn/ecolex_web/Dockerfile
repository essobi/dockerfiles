FROM python:3.6-slim  
  
# roles:  
# front - publishes ports to the world; this depends on run/docker-compose
though...  
# cron - runs cron daemon  
LABEL maintainer="daniel.baragan@eaudeweb.ro" \  
roles="front,cron" \  
name="web"  
  
RUN apt-get -y update &&\  
apt-get -y --no-install-recommends install \  
vim \  
sudo \  
netcat-traditional \  
git \  
libmariadb-client-lgpl-dev \  
gcc \  
libc-dev-bin \  
libc6-dev \  
make \  
patch \  
cron \  
curl \  
libyajl2 \  
sendmail \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV GNUPGHOME=/tmp/gnupghome \  
GOSU_VERSION=1.10  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" && \  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" && \  
mkdir $GNUPGHOME && \  
chmod og-rwx $GNUPGHOME && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true  
  
RUN ln -s /usr/bin/mariadb_config /usr/bin/mysql_config  
  
RUN adduser --disabled-password --gecos '' \--shell /bin/false web &&\  
adduser web sudo &&\  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# need to consume this anyway  
ENV ECOLEX_HOME=/home/web \  
PATH=/home/web/bin:$PATH \  
EDW_RUN_WEB_PORT=8000 \  
USER=web  
  
RUN mkdir -p $ECOLEX_HOME/ecolex &&\  
mkdir -p /www_static &&\  
mkdir -p $ECOLEX_HOME/bin  
  
# Add as few files of possible, we want to cache pip install step for good  
ADD docker/web/build/entrypoint.sh \  
docker/web/build/root-entrypoint.sh \  
docker/web/build/import_updater.sh \  
docker/web/build/reprocess_from_db.sh \  
$ECOLEX_HOME/bin/  
  
ADD docker/web/build/ecolex.crontab \  
$ECOLEX_HOME/  
  
ARG EDW_BUILD_SRC_DIR  
# Every time you change the value of this variable the cache will be skipped
from the next RUN step further  
#ARG EDW_ECOLEX_VER  
#RUN echo $EDW_ECOLEX_VER  
ADD requirements.txt \  
requirements-dep.txt \  
$ECOLEX_HOME/ecolex/  
  
WORKDIR $ECOLEX_HOME/ecolex  
RUN pip install -r requirements-dep.txt  
  
ADD . $ECOLEX_HOME/ecolex  
RUN chown -R web:web $ECOLEX_HOME  
  
RUN touch $ECOLEX_HOME/.bashrc  
RUN chmod 777 $ECOLEX_HOME/.bashrc  
# no changes to volume are persistent after declaring it  
VOLUME ["/www_static", "${ECOLEX_HOME}/logs"]  
  
# USER web # use gosu in the entrypoint  
ENTRYPOINT ["root-entrypoint.sh"]  
CMD ["run"]  

