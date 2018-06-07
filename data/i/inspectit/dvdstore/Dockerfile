FROM inspectit/jboss:5  
MAINTAINER info.inspectit@novatec-gmbh.de  
  
ENV PROJECT_NAME dvdstore  
  
#copy nessesary files and deplay dvdstore application  
RUN mkdir -p /database/database \  
&& mkdir -p /opt/agent/config/common  
  
WORKDIR /opt  
  
RUN wget -q ftp://ntftp.novatec-gmbh.de/inspectit/samples/sample-
dvdstore/${PROJECT_NAME}.zip \  
&& unzip ${PROJECT_NAME}.zip \  
&& mv h2.jar /database/ \  
&& ln -s /database/h2.jar /jboss-5.1.0.GA/server/default/lib/. \  
&& mv dvdstore22.h2.db /database/database/ \  
&& mv dvdstore22.trace.db /database/database/ \  
&& mv dvdstore.ear /jboss-5.1.0.GA/server/default/deploy/ \  
&& mv dvdstore-prod-ds.xml /jboss-5.1.0.GA/server/default/deploy/dvdstore-
ds.xml \  
&& mv inspectit-agent.cfg /opt/agent/config \  
&& mv dvdstore-*.cfg /opt/agent/config/common \  
&& rm -f ${PROJECT_NAME}.zip  
  
RUN apt-get update && apt-get install -y realpath  
RUN wget --no-check-certificate -O /wait-for-it.sh
https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
\  
&& chmod +x /wait-for-it.sh  

