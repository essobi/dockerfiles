FROM ubuntu:latest  
MAINTAINER chetan.ganatra@gmail.com  
  
ENV TIKA_VERSION 1.13  
ENV TIKA_SERVER_URL https://www.apache.org/dist/tika/tika-
server-$TIKA_VERSION.jar  
  
RUN apt-get -y update \  
&& apt-get -y install openjdk-8-jre-headless curl gdal-bin nodejs npm unzip \  
&& curl -sSL https://people.apache.org/keys/group/tika.asc -o /tmp/tika.asc \  
&& gpg \--import /tmp/tika.asc \  
&& curl -sSL "$TIKA_SERVER_URL.asc" -o /tmp/tika-
server-${TIKA_VERSION}.jar.asc \  
&& NEAREST_TIKA_SERVER_URL=$(curl -sSL
http://www.apache.org/dyn/closer.cgi/${TIKA_SERVER_URL#https://www.apache.org/dist/}\?asjson\=1
\  
| awk '/"path_info": / { pi=$2; }; /"preferred":/ { pref=$2; }; END { print
pref " " pi; };' \  
| sed -r -e 's/^"//; s/",$//; s/" "//') \  
&& echo "Nearest mirror: $NEAREST_TIKA_SERVER_URL" \  
&& curl -sSL "$NEAREST_TIKA_SERVER_URL" -o /tika-server-${TIKA_VERSION}.jar \  
&& gpg \--verify /tmp/tika-server-${TIKA_VERSION}.jar.asc /tika-
server-${TIKA_VERSION}.jar \  
&& apt-get -y clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir /docxtract && cd /docxtract && curl -sL
https://github.com/chetanganatra/docXtract/archive/master.zip -o master.zip \  
&& unzip master.zip -d . \  
&& curl -sL http://www.apache.org/dyn/closer.cgi/tika/tika-server-1.13.jar -o
/docxtract/tika-server-1.13.jar  
# RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
# RUN apt-get -y install nodejs  
# RUN apt-get -y install nodejs npm  
# RUN java -jar /tika-server-${TIKA_VERSION}.jar -h 0.0.0.0  
# EXPOSE 9998  

