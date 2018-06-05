FROM openjdk:jre-alpine  
  
ARG ATD_URL=http://www.polishmywriting.com/download/atd_distribution081310.tgz  
  
RUN busybox wget
http://www.polishmywriting.com/download/atd_distribution081310.tgz -O
atd_distribution.tgz && \  
tar -zxf atd_distribution.tgz -C /srv && \  
rm atd_distribution.tgz && \  
sed -i 's/127\\.0\\.0\\.1/0\\.0\\.0\\.0/g' /srv/atd/run.sh && \  
sed -i 's/-XX:+AggressiveHeap //g' /srv/atd/run.sh  
  
EXPOSE 1049  
  
WORKDIR /srv/atd  
  
CMD /srv/atd/run.sh  

