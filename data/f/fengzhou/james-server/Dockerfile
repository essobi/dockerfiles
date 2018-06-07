FROM java:8  
MAINTAINER Feng Zhou <feng.zh@gmail.com>  
  
ENV JAMES_HOME=/opt/local/james-server  
  
WORKDIR ${JAMES_HOME}  
  
COPY docker-setup.sh docker-entrypoint.sh ${JAMES_HOME}/  
  
RUN ${JAMES_HOME}/docker-setup.sh  
  
VOLUME /etc/james-server ${JAMES_HOME}/var  
  
EXPOSE 25 465 110 995 143 993  
CMD /bin/bash -e docker-entrypoint.sh  
  

