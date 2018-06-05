FROM alpine:3.6  
LABEL maintainer="Zabielski, Kamil <kamil.zabielski@outlook.com>"  
ENV BEANSTALKD_FSYNC_SECS=0  
EXPOSE 11300/TCP  
VOLUME [ "/var/lib/beanstalkd" ]  
  
RUN apk add --no-cache --update beanstalkd  
CMD beanstalkd -V -f"${BEANSTALKD_FSYNC_SECS}" -b /var/lib/beanstalkd  

