FROM java:7u121-jdk-alpine  
MAINTAINER Jiacai Liu jiacai2050@gmail.com  
  
ENV KESTREL_VERSION 2.4.1  
RUN set -xe \  
\  
&& wget -O kestrel.zip "http://twitter-
archive.github.io/kestrel/download/kestrel-$KESTREL_VERSION.zip" \  
&& mkdir /opt \  
&& ls -lh \  
&& unzip kestrel.zip -d /opt \  
&& rm kestrel.zip \  
&& ln -s /opt/kestrel-$KESTREL_VERSION /opt/kestrel  
  
ADD ./config.scala /opt/kestrel/config.scala  
  
WORKDIR /opt/kestrel  
  
EXPOSE 2222 2223 2229 22133  
# CMD & ENTRYPOINT doesn't expand ENV, so CMD below doesn't work  
# CMD ["/usr/bin/java", "-jar",
"/opt/kestrel/kestrel_2.9.2-$KESTREL_VERSION.jar", "-f",
"/opt/kestrel/config.scala"]  
# See: https://github.com/moby/moby/issues/4783  
CMD ["sh", "-c", "/usr/bin/java -jar
/opt/kestrel/kestrel_2.9.2-$KESTREL_VERSION.jar -f /opt/kestrel/config.scala"]

