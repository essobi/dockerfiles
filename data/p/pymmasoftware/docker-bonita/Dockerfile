FROM wmarinho/ubuntu:oracle-jdk-7  
MAINTAINER Wellington Marinho wpmarinho@globo.com  
  
ENV BONITA_VERSION 6.3.9  
ENV BONITA_HOME /opt/bos  
  
RUN apt-get update \  
&& apt-get install wget unzip git -y  
  
RUN wget -nv
http://download.forge.objectweb.org/bonita/BonitaBPMCommunity-${BONITA_VERSION}-Tomcat-6.0.37.zip
-O /tmp/BonitaBPMCommunity-${BONITA_VERSION}-Tomcat-6.0.37.zip  
  
RUN unzip -q /tmp/BonitaBPMCommunity-${BONITA_VERSION}-Tomcat-6.0.37.zip -d
/opt && mv /opt/Bonita* ${BONITA_HOME}  
  
RUN apt-get install postgresql-client-9.3 npm -y && npm install less -g  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
ADD config ${BONITA_HOME}/config/  
ADD scripts/setenv.sh ${BONITA_HOME}/bin/  
ADD scripts ${BONITA_HOME}/bin/  
  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/' ${BONITA_HOME}/bin/startup.sh  
  
EXPOSE 8080  
CMD ["/opt/bos/bin/run.sh"]  

