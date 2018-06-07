FROM docker.elastic.co/kibana/kibana:6.2.4  
MAINTAINER Inspectorio DevOps <devops@inspectorio.com>  
  
ENV ES_VERSION 6.2.4  
ENV LOGTRAIL_VERSION 0.1.27  
RUN ./bin/kibana-plugin install
"https://github.com/sivasamyk/logtrail/releases/download/v${LOGTRAIL_VERSION}/logtrail-${ES_VERSION}-${LOGTRAIL_VERSION}.zip"  

