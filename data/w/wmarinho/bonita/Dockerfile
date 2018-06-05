FROM java:openjdk-8  
MAINTAINER Wellington Marinho wpmarinho@globo.com  
  
ENV BONITA_VERSION 6.5.1  
ENV TOMCAT_VERSION 7.0.55  
ENV PGSQL_VERSION 9.4  
ENV PGSQL_BUILD 9.4-1201  
ENV BONITA_HOME /opt/bos  
  
RUN apt-get update \  
&& apt-get install wget unzip git -y  
  
RUN wget -nv
http://download.forge.objectweb.org/bonita/BonitaBPMCommunity-${BONITA_VERSION}-Tomcat-${TOMCAT_VERSION}.zip
-O /tmp/bos.zip  
  
RUN unzip -q /tmp/bos.zip -d /opt && mv /opt/Bonita* ${BONITA_HOME}  
  
RUN apt-get install postgresql-client-${PGSQL_VERSION} npm -y && npm install
less -g  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
ADD config ${BONITA_HOME}/config/  
ADD scripts/setenv.sh ${BONITA_HOME}/bin/  
ADD scripts ${BONITA_HOME}/bin/  
  
RUN sed -i -e 's/\\(exec ".*"\\) start/\1 run/' ${BONITA_HOME}/bin/startup.sh  
  
EXPOSE 8080  
CMD ["/opt/bos/bin/run.sh"]  

