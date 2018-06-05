FROM java:7  
MAINTAINER Chris Renzo Chris.renzo@technekes.com  
EXPOSE 8080  
WORKDIR /tmp/interlok/  
  
RUN apt-get update && \  
apt-get -y install vim ant xsltproc && \  
apt-get clean && \  
cd /var/lib/apt/lists && rm -fr *Release* *Sources* *Packages* && \  
truncate -s 0 /var/log/*log  
  
ENV ADAPTRIS_VER=3.0.6  
COPY install.ini /tmp/interlok/install.ini  
  
RUN wget
http://development.adaptris.net/installers/Interlok/${ADAPTRIS_VER}/install.bin
&& \  
chmod +x install.bin && \  
sh install.bin -f install.ini && \  
rm -rf /tmp/interlok  
  
WORKDIR /opt/interlok  
  
COPY ant/build.xml /opt/interlok/ant/build.xml  
COPY ant/build.properties /opt/interlok/ant/build.properties  
COPY ant/resources/ivy-interlok.xml /opt/interlok/ant/resources/ivy-
interlok.xml  
COPY ant/resources/ivy-settings.xml /opt/interlok/ant/resources/ivy-
settings.xml  
  
RUN cd ant && \  
ant deploy && \  
cp /opt/interlok/ant/lib/* /opt/interlok/lib/ && \  
rm -rf /opt/interlok/ant  
  
ENTRYPOINT ["/bin/bash"]  

