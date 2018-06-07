# This is a hideously ugly Dockerfile, but if we want an image with a minimum  
# of layers we are more-or-less forced to do it this way.  
#  
# Important notes:  
# 1\. EVERY LINE MUST END WITH A BACKSLASH!  
# 2\. Even blank lines need a trailing backslash.  
# 3\. Each command is terminated by a semicolon.  
# 4\. Did I mention that EVERY LINE MUST END WITH A BACKSLASH?  
#  
# Why is there no MAINTAINER command? Because that creates another bloody  
# layer! We're going for minimal here...  
#  
# Docker hates you and wishes you would just go away and leave it alone.  
  
FROM buildpack-deps:jessie  
RUN \  
export DEBIAN_FRONTEND=noninteractive; \  
apt-get update; \  
apt-get -y --no-install-recommends install \  
python2.7 python2.7-dev \  
python3.4 python3.4-dev \  
python3-pip; \  
\  
pip3 install tox; \  
\  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \  
# END RUN  
  
  
# Install gosu to run tox as the "tox" user instead of as root.  
# https://github.com/tianon/gosu#from-debian  
#ENV GOSU_VERSION 1.7  
#RUN set -x && \  
# apt-get update && \  
# apt-get install -y --no-install-recommends ca-certificates wget && \  
# rm -rf /var/lib/apt/lists/* && \  
# wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" && \  
# wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" && \  
# export GNUPGHOME="$(mktemp -d)" && \  
# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
# gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \  
# rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc && \  
# chmod +x /usr/local/bin/gosu && \  
# gosu nobody true && \  
# apt-get purge -y --auto-remove ca-certificates wget  
#  
# Install PyPy3 and source.  
#RUN mkdir /install && \  
# wget -O /install/pypy3-2.4-linux_x86_64-portable.tar.bz2 \  
# "https://bitbucket.org/squeaky/portable-
pypy/downloads/pypy3-2.4-linux_x86_64-portable.tar.bz2" && \  
# tar jxf /install/pypy3-*.tar.bz2 -C /install && \  
# rm /install/pypy3-*.tar.bz2 && \  
# chown -R root:root /install/pypy3-* && \  
# mv /install/pypy3-* /usr/lib/pypy3 && \  
# rm -rf /install && \  
# ln -s /usr/lib/pypy3/bin/pypy3 /usr/local/bin/pypy3  
#  
#  
#WORKDIR /app  
#VOLUME /src  
#  
#ONBUILD COPY install-prereqs*.sh requirements*.txt tox.ini /app/  
#ONBUILD ARG SKIP_TOX=false  
#ONBUILD RUN bash -c " \  
# if [ -f '/app/install-prereqs.sh' ]; then \  
# bash /app/install-prereqs.sh; \  
# fi && \  
# if [ $SKIP_TOX == false ]; then \  
# TOXBUILD=true tox; \  
# fi"  
#  
#COPY docker-entrypoint.sh /  
#  
#ENTRYPOINT ["/docker-entrypoint.sh"]  
#CMD ["tox"]  

