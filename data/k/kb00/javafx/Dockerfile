FROM i386/ubuntu  
MAINTAINER Kirill Bychkov <kb@na.ru>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=linux \  
INITRD=No \  
LANGUAGE=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LC_CTYPE=en_US.UTF-8 \  
LC_MESSAGES=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
GOSU_VERSION=1.10 \  
TINI_VERSION=v0.14.0  
# install utilities  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -y apt-utils ssh curl \  
&& apt-get install -y rpm fakeroot libxml2 libxml2-utils libxslt1.1
libgtk2.0-0 libxtst6 \  
&& apt-get install -y --no-install-recommends ca-certificates wget  
  
# create locales  
RUN apt-get install -y locales \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias
ru_RU.UTF-8  
  
# setup default locale  
ENV LANG en_US.utf8  
  
# install gosu  
RUN set -x && \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
&& \  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
&& \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \  
rm -r /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true  
  
# install tini  
RUN set -x && \  
wget -O /usr/local/bin/tini
"https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" && \  
wget -O /usr/local/bin/tini.asc
"https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc"
&& \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 && \  
gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini && \  
rm -r "$GNUPGHOME" /usr/local/bin/tini.asc && \  
chmod +x /usr/local/bin/tini  
  
# clear apt cache  
RUN apt-get purge -y --auto-remove ca-certificates wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Oracle JDK 8u131  
RUN mkdir /srv/java && cd /tmp && \  
curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k
"http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-i586.tar.gz"
&& \  
tar xf jdk-8u131-linux-i586.tar.gz -C /srv/java && \  
rm -f jdk-8u131-linux-i586.tar.gz && \  
ln -s /srv/java/jdk* /srv/java/jdk && \  
ln -s /srv/java/jdk /srv/java/jvm  
  
# Define JAVA_HOME variable  
# Add /srv/java and jdk on PATH variable  
ENV JAVA_HOME=/srv/java/jdk \  
PATH=${PATH}:/srv/java/jdk/bin:/srv/java  
  
# Define default command.  
CMD [ "/bin/bash", "-l"]

