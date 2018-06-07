FROM debian:jessie  
  
MAINTAINER Pouya Tafti <pouya@nohup.io>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ENV LOCAL_USER=user  
ENV LOCAL_UID=1001  
ENV LOCAL_GROUP=group  
ENV LOCAL_GID=1001  
# create default group  
RUN groupadd -g 1000 default  
  
# install os-level pkgs  
RUN apt-get clean && \  
apt-get update --fix-missing && \  
apt-get install --no-install-recommends --no-install-suggests -y \  
wget ca-certificates \  
curl grep sed dpkg gnupg \  
&& \  
apt-get clean  
  
# install tini  
RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep
-o "/tag.*\"" | sed 's:^.....\\(.*\\).$:\1:'` && \  
wget -O /bin/tini
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini && \  
wget -O /bin/tini.asc
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc &&
\  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 && \  
gpg --verify /bin/tini.asc && \  
rm -r "$GNUPGHOME" /bin/tini.asc && \  
chmod +x /bin/tini  
  
# install gosu  
RUN GOSU_VERSION=`curl https://github.com/tianon/gosu/releases/latest | grep
-o "/tag.*\"" | sed 's:^.....\\(.*\\).$:\1:'` && \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
wget -O /bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
&& \  
wget -O /bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
&& \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
gpg --verify /bin/gosu.asc && \  
rm -r "$GNUPGHOME" /bin/gosu.asc && \  
chmod +x /bin/gosu && \  
gosu nobody true  
  
# install entry point  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod 755 /docker-entrypoint.sh  
  
# entry point  
ENTRYPOINT ["/bin/tini", "--", "/docker-entrypoint.sh"]  

