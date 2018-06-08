FROM veltio/pentaho:latest  
MAINTAINER Gleison Silva "geison.silva@gmail.com"  
  
RUN wget -c -nv --no-check-certificate https://googledrive.com/host/0B4pi-
CIMz3h1YmgyYmRlVGJVUkE/ppa-pp.zip \  
-O /tmp/ppa-pp.zip && \  
unzip /tmp/ppa-pp.zip -d /opt/pentaho/biserver-ce/pentaho-solutions/system/  
  
RUN cp /opt/pentaho/biserver-ce/pentaho-
solutions/system/ppa/patches/tomcat/lib/* \  
/opt/pentaho/biserver-ce/tomcat/lib/  
  
EXPOSE 8080  
  
CMD ["/assets/init"]

