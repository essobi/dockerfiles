# from https://github.com/dockerfile/java/blob/master/oracle-java8/Dockerfile  
# The MIT License (MIT)  
# Copyright (c) Dockerfile Project  
#  
FROM ubuntu:14.04  
RUN \  
sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list && \  
sed -i 's/security.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list  
# sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN \  
apt-get update && \  
apt-get upgrade -y  
  
# 한글 설정  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
RUN apt-get install -y language-pack-ko  
RUN locale-gen ko_KR.UTF-8  
ADD config/.vimrc /root/.vimrc  
  
RUN \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define working directory.  
WORKDIR /data  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV ES_PKG_NAME elasticsearch-1.7.0  
RUN \  
apt-get update &&\  
apt-get install -y automake perl build-essential  
  
RUN \  
apt-get install -y mysql-client  
  
# Install Elasticsearch.  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
RUN \  
cd /opt &&\  
wget https://bitbucket.org/eunjeon/mecab-
ko/downloads/mecab-0.996-ko-0.9.2.tar.gz &&\  
tar xvf mecab-0.996-ko-0.9.2.tar.gz &&\  
cd /opt/mecab-0.996-ko-0.9.2 &&\  
./configure &&\  
make &&\  
make check &&\  
make install &&\  
ldconfig  
  
RUN \  
cd /opt &&\  
wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-
dic-2.0.1-20150825.tar.gz &&\  
tar xvf mecab-ko-dic-2.0.1-20150825.tar.gz &&\  
cd /opt/mecab-ko-dic-2.0.1-20150825 &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
make install  
  
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8  
  
RUN \  
cd /opt &&\  
wget https://mecab.googlecode.com/files/mecab-java-0.996.tar.gz &&\  
tar xvf mecab-java-0.996.tar.gz &&\  
cd /opt/mecab-java-0.996 &&\  
sed -i
's|/usr/lib/jvm/java-6-openjdk/include|/usr/lib/jvm/java-8-oracle/include|'
Makefile &&\  
make &&\  
cp libMeCab.so /usr/local/lib  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
RUN /elasticsearch/bin/plugin --install analysis-mecab-ko-0.17.0 --url
https://bitbucket.org/eunjeon/mecab-ko-lucene-
analyzer/downloads/elasticsearch-analysis-mecab-ko-0.17.0.zip  
  
# Install Plugin  
RUN /elasticsearch/bin/plugin --install mobz/elasticsearch-head  
RUN /elasticsearch/bin/plugin --install river-csv --url
https://github.com/AgileWorksOrg/elasticsearch-river-
csv/releases/download/2.2.1/elasticsearch-river-csv-2.2.1.zip  
RUN /elasticsearch/bin/plugin --install sql --url
https://github.com/NLPchina/elasticsearch-
sql/releases/download/1.3.5/elasticsearch-sql-1.3.5.zip  
  
# Define working directory.  
WORKDIR /data  
  
# Ruby install  
# sudo gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
# curl -L https://get.rvm.io | sudo bash -s stable  
# exec su -l  
# rvm install 2.0.0  
# gem update --system  
# gem install mysql2xxxx  
# Php install  
# Define default command.  
CMD /elasticsearch/bin/elasticsearch -Djava.library.path=/usr/local/lib  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  

