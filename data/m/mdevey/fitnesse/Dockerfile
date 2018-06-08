# Fitnesse  
#  
#  
FROM ubuntu:latest  
MAINTAINER Ruggero Marchei <ruggero.marchei@daemonzone.net>  
  
  
RUN groupadd -r fitnesse --gid=888 \  
&& useradd -d /opt/fitnesse -m -s /bin/bash -r -g fitnesse --uid=888 fitnesse  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common unzip curl && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
ENV GOSU_VERSION 1.7  
RUN cd /usr/local/bin \  
&& curl -fsSL -o gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& curl -fsSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/SHA256SUMS" |
grep -E 'gosu-amd64$' | sed -e 's/gosu-.*$/gosu/' | sha256sum -c - \  
&& chmod +x gosu  
  
ENV FITNESSE_RELEASE 20151230  
RUN mkdir -p /opt/fitnesse/FitNesseRoot \  
&& curl -fsSL -o /opt/fitnesse/fitnesse-standalone.jar
"http://www.fitnesse.org/fitnesse-
standalone.jar?responder=releaseDownload&release=$FITNESSE_RELEASE" \  
&& chown -R fitnesse.fitnesse /opt/fitnesse  
  
COPY docker-entrypoint.sh /bin/  
RUN chmod +x /bin/docker-entrypoint.sh  
  
VOLUME /opt/fitnesse/FitNesseRoot  
EXPOSE 80  
WORKDIR /opt/fitnesse  
  
ENTRYPOINT ["/bin/docker-entrypoint.sh"]  

