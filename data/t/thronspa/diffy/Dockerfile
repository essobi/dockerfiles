FROM java:8u111-jre-alpine  
MAINTAINER THRON Devops <devops@thron.com>  
  
ENV DIFFY_PATH=/opt/src/diffy  
  
RUN apk add --update \  
bash \  
curl \  
git \  
nodejs \  
openssl \  
&& rm -rf /var/cache/apk/* \  
&& npm install -g duplicator  
  
RUN mkdir -p ${DIFFY_PATH} && cd ${DIFFY_PATH} \  
&& git clone https://github.com/twitter/diffy.git . \  
&& ./sbt assembly  
  
COPY files/ /  
  
RUN chmod +x /etc/docker/start.sh && dos2unix /etc/docker/start.sh  
  
CMD ["/etc/docker/start.sh"]  
  
EXPOSE 80 31149 31159

