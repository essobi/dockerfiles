FROM dtank/core:latest  
  
MAINTAINER benharker@mac.com  
  
RUN wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add - && echo "deb
http://ppa.moosefs.com/current/apt/ubuntu/trusty trusty main" >>
/etc/apt/sources.list.d/moosefs.list ;  
RUN apt-get update ; apt-get install -y moosefs-chunkserver nano ; rm -rf
/var/lib/apt/lists/* && mv /etc/mfs/mfschunkserver.cfg.sample
/etc/mfs/mfschunkserver.cfg ; mv /etc/mfs/mfshdd.cfg.sample
/etc/mfs/mfshdd.cfg ; echo "/mfschunks/ 1GiB" >> /etc/mfs/mfshdd.cfg ;  
  
COPY ./run-chunk /usr/local/bin/run-chunk  
RUN chmod -Rv 777 /usr/local/bin/* ;  
  
EXPOSE 9420  
EXPOSE 9422  
CMD ["/usr/local/bin/run-chunk"]  

