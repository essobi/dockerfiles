# DavMail service  
# See https://github.com/iron-io/dockers/tree/master/java/java-1.8  
FROM iron/java:1.8  
MAINTAINER Kayvan Sylvan <kayvansylvan@gmail.com>  
  
RUN mkdir -p /opt/davmail && \  
wget -q -O -
http://downloads.sourceforge.net/project/davmail/davmail/4.7.2/davmail-
linux-x86_64-4.7.2-2427.tgz | \  
tar -C /opt/davmail -xvz  
RUN mv /opt/davmail/davmail-linux-x86_64-4.7.2-2427/* /opt/davmail && rmdir
/opt/davmail/davmail-linux-x86_64-4.7.2-2427  
  
EXPOSE 1080  
EXPOSE 1143  
EXPOSE 1389  
EXPOSE 1110  
EXPOSE 1025  
WORKDIR /opt/davmail  
CMD ["/etc/davmail/davmail.properties"]  
ENTRYPOINT ["/opt/davmail/davmail.sh"]  

