FROM cyberluisda/openjdk:8  
  
MAINTAINER Luis David Barrios Alfonso (luisdavid.barrios@agsnasoft.com /
cyberluisda@gmail.com)  
  
#install ivy  
RUN apt-get update && apt-get install -y ivy gawk && rm -rf
/var/lib/apt/lists/*  
  
ENV FLUME_VERSION 1.7.0  
ADD http://apache.rediris.es/flume/${FLUME_VERSION}/apache-
flume-${FLUME_VERSION}-bin.tar.gz /usr/var/lib/  
RUN cd /usr/var/lib/ && tar -zxvf apache-flume-${FLUME_VERSION}-bin.tar.gz >
/dev/null && rm -f apache-flume-${FLUME_VERSION}-bin.tar.gz && cd \- >
/dev/null  
RUN mv /usr/var/lib/apache-flume-1.7.0-bin /usr/var/lib/flume  
  
ENV PATH /usr/var/lib/flume/bin:$PATH  
#Add Dep libs  
RUN mkdir -p /opt/flume-third/lib  
COPY files/ivy.xml /usr/var/lib/flume/conf  
COPY files/ivy-settings.xml /usr/var/lib/flume/conf  
RUN java -jar /usr/share/java/ivy.jar -settings /usr/var/lib/flume/conf/ivy-
settings.xml -ivy /usr/var/lib/flume/conf/ivy.xml -retrieve
"/usr/var/lib/flume/lib/[artifact].[ext]"  
  
ADD files/entry_point.sh /usr/var/lib/flume/bin  
RUN chmod a+x /usr/var/lib/flume/bin/entry_point.sh  
  
ADD files/flume-env.sh /usr/var/lib/flume/conf  
  
RUN mkdir -p /etc/flume /var/log/flume /var/flume/sources /var/flume/extra-
libs  
VOLUME /etc/flume /var/flume/ingestion /var/flume/sources /var/flume/extra-
libs  
  
COPY files/parametrize.awk /usr/var/lib/flume/bin  
#Add dockerize tool  
ENV DOCKERIZE_VERSION v0.5.0  
RUN curl -L
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
| tar -C /usr/local/bin -xzvf -  
  
ENTRYPOINT ["entry_point.sh"]  
CMD ["--help"]  

