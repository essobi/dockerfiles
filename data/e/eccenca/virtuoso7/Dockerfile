####  
#  
# Dockerfile for building an OpenLink Virtuoso Opensource from git.  
# Virtuoso config is provided here.  
#  
# Installation is in /opt/virtuoso-opensource, the database files reside in
/var/lib/virtuoso/db/  
####  
FROM eccenca/baseimage:1.0.1  
MAINTAINER Rene Pietzsch <rene.pietzsch@eccenca.com>  
MAINTAINER Henri Knochehauer <henri.knochenhauer@eccenca.com>  
  
ENV VIRT_HOME /opt/virtuoso-opensource  
ENV VIRT_INI_TEMPLATE /var/lib/virtuoso/virtuoso_template.ini  
ENV VIRT_DB /var/lib/virtuoso/db  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install dpkg-dev build-essential && \  
apt-get -y install autoconf automake libtool flex bison git && \  
apt-get -y install gperf gawk m4 make openssl libssl-dev  
  
# Clone virtuoso  
WORKDIR /opt  
RUN git clone https://github.com/openlink/virtuoso-opensource.git virtuoso-
opensource.src  
WORKDIR /opt/virtuoso-opensource.src  
RUN git checkout v7.2.0.1  
# Fix for date on Ubuntu 14.04  
# RUN git config user.email "docker@eccenca.com"  
# RUN git config user.name "Docker"  
# RUN git cherry-pick 042f1427380e3a474581f4aa1ee064f5d2da9963  
RUN ./autogen.sh && ./configure --prefix=$VIRT_HOME && make && make install  
  
RUN mkdir -p $VIRT_DB/  
ADD virtuoso.ini $VIRT_INI_TEMPLATE  
ADD ./my_init.d /etc/my_init.d  
ADD ./svc /etc/service  
  
ADD assets/virtuoso_helper.sh /$VIRT_HOME/virtuoso_helper.sh  
RUN chmod +x /$VIRT_HOME/virtuoso_helper.sh  
  
EXPOSE 1111  
EXPOSE 8890  
VOLUME ["/var/lib/virtuoso/db"]  
CMD ["/sbin/my_init"]

