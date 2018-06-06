FROM debian  
MAINTAINER rkernan@gmail.com  
COPY 100-ubnt.list /etc/apt/sources.list.d/100-ubnt.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50  
RUN apt-get -q --assume-no update && apt-get install -qy unifi  
VOLUME /usr/lib/unifi/data  
VOLUME /usr/lib/unifi/logs  
EXPOSE 8080 8443 8880 8843  
WORKDIR /usr/lib/unifi  
CMD ["/usr/bin/java", "-jar", "lib/ace.jar", "start"]  

