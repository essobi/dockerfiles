# Use phusion/baseimage as base image  
# Logicaldoc Document Management System ( http://www.logicaldoc.com )  
FROM phusion/baseimage:0.9.18  
MAINTAINER "Mihai Csaky" <mihai.csaky@sysop-consulting.ro>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# ...put your own build instructions here...  
ENV MYSQL_SERVER mysql-server-5.6  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV CATALINA_HOME /opt/logicaldoc/tomcat  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  
ENV DATADIR /var/lib/mysql  
  
# prepare system for mysql installation  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y perl pwgen --no-install-recommends  
  
# install mysql  
RUN apt-get install -y ${MYSQL_SERVER} \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
# prepare system for java installation  
RUN apt-get -y install software-properties-common python-software-properties  
  
# install oracle java  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
  
# some required software for logicaldoc plugins  
RUN apt-get -y install \  
libreoffice \  
imagemagick \  
swftools \  
liblog4j1.2-java \  
libgnumail-java \  
ant \  
curl \  
unzip \  
sudo \  
tar \  
ghostscript \  
xpdf \  
tesseract-ocr  
  
#download and unzip logicaldoc installer  
RUN mkdir /opt/logicaldoc  
RUN curl -L
http://netcologne.dl.sourceforge.net/project/logicaldoc/distribution/LogicalDOC%20CE%207.4/logicaldoc-
community-installer-7.4.3.zip \  
-o /opt/logicaldoc/logicaldoc-community-installer-7.4.3.zip && \  
unzip /opt/logicaldoc/logicaldoc-community-installer-7.4.3.zip -d
/opt/logicaldoc && \  
rm /opt/logicaldoc/logicaldoc-community-installer-7.4.3.zip  
  
#add configuration scripts  
ADD 01_mysql.sh /etc/my_init.d/  
ADD 02_logicaldoc.sh /etc/my_init.d/  
ADD wait-for-it.sh /opt/logicaldoc  
ADD auto-install.xml /opt/logicaldoc  
  
#volumes for persistent storage  
VOLUME /var/lib/mysql  
VOLUME /opt/logicaldoc/repository  
  
#port to connect to  
EXPOSE 8080  
#mysql service setup  
RUN mkdir /etc/service/mysqld/  
ADD mysqld.sh /etc/service/mysqld/run  
  
#logicaldoc service setup  
RUN mkdir /etc/service/logicaldoc/  
ADD logicaldoc.sh /etc/service/logicaldoc/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

