FROM dtank/core:latest  
  
MAINTAINER benharker@mac.com  
  
RUN wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add - && echo "deb
http://ppa.moosefs.com/current/apt/ubuntu/trusty trusty main" >>
/etc/apt/sources.list.d/moosefs.list ;  
RUN apt-get update ; apt-get install -y moosefs-master nano ; rm -rf
/var/lib/apt/lists/* && mv /etc/mfs/mfsexports.cfg.sample
/etc/mfs/mfsexports.cfg ; mv /etc/mfs/mfsmaster.cfg.sample
/etc/mfs/mfsmaster.cfg ;  
  
EXPOSE 9419  
EXPOSE 9420  
EXPOSE 9421  
COPY ./run-master /usr/local/bin/run-master  
RUN chmod -Rv 777 /usr/local/bin/* ;  
  
CMD ["/usr/local/bin/run-master"]  

