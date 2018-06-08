# vim:set ft=dockerfile:  
FROM ubuntu:latest  
  
# we like gosu  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN mkdir /usr/lib/java-1.8.0 \  
&& /usr/bin/wget http://download.oracle.com/otn-pub/java/jdk/8u65-b17/server-
jre-8u65-linux-x64.tar.gz --no-cookies --header 'Cookie: oraclelicense=accept-
securebackup-cookie' \  
&& tar -C /usr/lib/java-1.8.0 --strip-components=1 -zxf server-
jre-8u65-linux-x64.tar.gz \  
&& rm -f server-jre-8u65-linux-x64.tar.gz  
  
COPY java.env.sh /etc/profile.d/java.sh  
  
RUN mkdir /usr/lib/jolokia \  
&& /usr/bin/wget
https://github.com/rhuss/jolokia/releases/download/v1.3.2/jolokia-1.3.2-bin.tar.gz
\  
&& tar -C --strip-components=1 /usr/lib/jolokia -zxf jolokia-1.3.2-bin.tar.gz
\  
&& rm -f jolokia-1.3.2-bin.tar.gz  
  
CMD /bin/true  

