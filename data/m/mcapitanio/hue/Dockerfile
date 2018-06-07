FROM mcapitanio/centos-java:7-7u80  
  
MAINTAINER Matteo Capitanio <matteo.capitanio@gmail.com>  
  
USER root  
  
ENV HUE_VER 4.0.0  
ENV HUE_HOME /opt/hue  
  
ENV PATH $HUE_HOME/build/env/bin:$PATH  
  
# Install needed packages  
RUN yum update -y; \  
yum upgrade -y  
RUN yum install -y \  
ant \  
asciidoc \  
cyrus-sasl-devel \  
cyrus-sasl-gssapi \  
cyrus-sasl-plain \  
gcc \  
gcc-c++ \  
krb5-devel \  
libffi-devel \  
libxml2-devel \  
libxslt-devel \  
make \  
maven \  
mysql \  
mysql-devel \  
openldap-devel \  
python-devel \  
python-pip \  
python-setuptools \  
sqlite-devel \  
openssl-devel \  
gmp-devel \  
rsynch \  
snappy \  
snappy-devel \  
libtidy \  
libtidy-devel \  
openssl \  
postgresql \  
postgresql-devel \  
epel-release  
RUN yum install -y python-pip  
RUN easy_install supervisor  
RUN pip install --upgrade pip  
RUN pip install setuptools psycopg2  
RUN yum clean all  
  
WORKDIR /opt/docker  
  
# Cloudera Hue  
RUN wget https://github.com/cloudera/hue/archive/release-$HUE_VER.tar.gz  
RUN tar -xvf release-$HUE_VER.tar.gz  
RUN mv hue-release-$HUE_VER $HUE_HOME  
  
COPY etc/ /etc/  
  
RUN useradd -p $(echo "hue" | openssl passwd -1 -stdin) hue; \  
useradd -p $(echo "hdfs" | openssl passwd -1 -stdin) hdfs; \  
groupadd supergroup; \  
usermod -a -G supergroup hue; \  
usermod -a -G hdfs hue  
  
RUN cd $HUE_HOME; \  
make apps  
  
RUN rm -rf $HUE_HOME/desktop/conf.dist  
  
COPY hue/ $HUE_HOME/  
  
RUN chmod +x $HUE_HOME/build/env/bin/*.sh  
  
VOLUME [ "/opt/hue/conf", "/opt/hue/logs" ]  
  
EXPOSE 8000  
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

