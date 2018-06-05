FROM ngnjs/base  
MAINTAINER Corey Butler  
  
#ADD ./app /app  
  
# Add Dependencies  
RUN apk add --update zeromq zeromq-dev pkgconfig python gcc g++ make bash \  
&& cd / \  
&& npm install zmq ngn-sse socket.io \  
# && cd /app \  
# && npm install \  
&& apk del zeromq-dev pkgconfig python gcc g++ make #bash  
  
RUN echo "#!/bin/sh" > /launch.sh \  
&& echo "export DOCKER_HOST=`netstat -nr | grep '^0\\.0\\.0\\.0' | awk '{print
$2}'`" >> /launch.sh \  
&& echo "/bin/bash" >> /launch.sh \  
&& chmod +x /launch.sh \  
&& cat /launch.sh  
  
EXPOSE 443 5555  
  
  
CMD ["/launch.sh"]  
#export DOCKER_HOST=`netstat -nr | grep '^0\\.0\\.0\\.0' | awk '{print $2}'`  
#CMD ["node","index.js"]  
  
#ADD gnatsd /gnatsd  
#ADD gnatsd.conf /gnatsd.conf  
#  
## Expose client, management, and routing/cluster ports  
#EXPOSE 4222 8222 6222  
#  
#ENTRYPOINT ["/gnatsd", "-c", "/gnatsd.conf"]  

