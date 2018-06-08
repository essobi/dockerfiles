FROM debian:jessie  
MAINTAINER Chris Jones <chris@sysadminchris.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" \  
> /etc/apt/sources.list.d/20ubiquiti.list  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main"
\  
> /etc/apt/sources.list.d/21mongodb.list  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
  
RUN mkdir /var/lib/unifi && chown -R nobody.nogroup /var/lib/unifi  
RUN mkdir /var/log/unifi && chown -R nobody.nogroup /var/log/unifi  
RUN mkdir /var/run/unifi && chown -R nobody.nogroup /var/run/unifi  
  
RUN apt-get -q update && \  
apt-get install -qy unifi && \  
apt-get -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /var/lib/unifi /usr/lib/unifi/data  
EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp  
  
RUN chown -R nobody.nogroup /usr/lib/unifi  
USER nobody  
  
VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi",
"/usr/lib/unifi/work"]  
  
WORKDIR /var/lib/unifi  
  
ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar"]  
CMD ["start"]  
  

