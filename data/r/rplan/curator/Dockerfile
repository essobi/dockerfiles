FROM alpine:3.7  
RUN apk --no-cache add python py-pip \  
&& pip install elasticsearch-curator==5.4.1  
  
STOPSIGNAL SIGKILL  
COPY ./files /  
  
CMD ["crond", "-f", "-d", "8", "-l", "8"]  

