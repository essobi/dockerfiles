# davmail service  
#  
# This Dockerfile will build a davmail docker image  
FROM ubuntu:12.04  
MAINTAINER BK Box "bk@theboxes.org"  
RUN apt-get update  
RUN apt-get install -y default-jre wget  
RUN apt-get clean  
RUN mkdir /usr/local/davmail  
RUN wget -O -
http://downloads.sourceforge.net/project/davmail/davmail/4.3.3/davmail-
linux-x86_64-4.3.3-2146.tgz | tar -C /usr/local/davmail --strip-components=1
-xvz  
  
# Cleanup for a smaller image  
RUN apt-get clean  
RUN rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*  
  
#VOLUME /etc/davmail  
EXPOSE 1080  
EXPOSE 1143  
EXPOSE 1389  
EXPOSE 1110  
EXPOSE 1025  
WORKDIR /usr/local/davmail  
CMD ["/etc/davmail/davmail.properties"]  
ENTRYPOINT ["/usr/local/davmail/davmail.sh"]  

