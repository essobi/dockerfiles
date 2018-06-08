FROM centos:7  
MAINTAINER Jordan Wesolowski <jrwesolo@gmail.com>  
  
# EPEL required for python-pip  
RUN yum install -y epel-release && \  
yum install -y createrepo python-pip PyYAML && \  
yum clean all  
  
ENV PAKRAT_VERSION=0.3.2  
RUN pip install pakrat==$PAKRAT_VERSION  
  
# gosu install  
ENV GOSU_VERSION 1.4  
RUN curl -o /usr/local/bin/gosu -sSL
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64 && \  
curl -o /usr/local/bin/gosu.asc -sSL
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64.asc
&& \  
gpg -q --keyserver pgp.mit.edu --recv-keys BF357DD4 && \  
gpg --verify /usr/local/bin/gosu.asc && \  
rm /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu  
  
ENV PAKRAT_CONF=/etc/pakrat \  
PAKRAT_DATA=/data/pakrat \  
PAKRAT_USER=pakrat PAKRAT_UID=489 \  
PAKRAT_GROUP=pakrat PAKRAT_GID=489  
RUN groupadd -g $PAKRAT_GID $PAKRAT_GROUP && \  
useradd -s /bin/bash -M -N -u $PAKRAT_UID -g $PAKRAT_GROUP $PAKRAT_USER && \  
mkdir -p $PAKRAT_DATA $PAKRAT_CONF && \  
chown $PAKRAT_USER:$PAKRAT_GROUP $PAKRAT_DATA $PAKRAT_CONF && \  
chmod 0755 $PAKRAT_DATA $PAKRAT_CONF  
  
COPY pakratsync pakratsetup /usr/local/bin/  
  
VOLUME $PAKRAT_DATA  
ENTRYPOINT ["/usr/local/bin/pakratsetup"]  
CMD []  

