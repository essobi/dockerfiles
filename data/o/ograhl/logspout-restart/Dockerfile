FROM alpine  
MAINTAINER Oliver Grahl <og@grahl-software.com>  
  
RUN apk --no-cache add curl  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
ENV FREQ_SECS=10  
CMD ["/run.sh"]  

