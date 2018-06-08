# Fitnesse  
#  
#  
FROM centos:latest  
MAINTAINER Nathan Rhoda <nathan.rhoda@euromonitor.com>  
  
  
RUN groupadd -r fitnesse --gid=888 \  
&& useradd -d /opt/fitnesse -m -s /bin/bash -r -g fitnesse --uid=888 fitnesse  
  
  
ENV GOSU_VERSION 1.7  
RUN cd /usr/local/bin \  
&& curl -fsSL -o gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& curl -fsSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/SHA256SUMS" |
grep -E 'gosu-amd64$' | sed -e 's/gosu-.*$/gosu/' | sha256sum -c - \  
&& chmod +x gosu  
  
  
RUN yum install -y java-1.8.0-openjdk-headless unzip \  
&& yum clean all -q  
  
  
  
ENV FITNESSE_RELEASE 20151230  
RUN mkdir -p /opt/fitnesse/FitNesseRoot \  
&& curl -fsSL -o /opt/fitnesse/fitnesse-standalone.jar
"http://www.fitnesse.org/fitnesse-
standalone.jar?responder=releaseDownload&release=$FITNESSE_RELEASE" \  
&& chown -R fitnesse.fitnesse /opt/fitnesse  
  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
VOLUME /opt/fitnesse/FitNesseRoot  
EXPOSE 80  
WORKDIR /opt/fitnesse  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

