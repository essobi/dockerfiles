FROM alpine:3.4  
RUN env > /tmp/env.txt  
RUN set > /tmp/set.txt  
ADD
https://github.com/udistrital/kronos_api_crud/releases/download/v0.0.0/kronos_api_crud.linux.amd64
/usr/bin/kronos_api_crud  
RUN chmod +x /usr/bin/kronos_api_crud  
EXPOSE 8080  
ENV GOPATH=/root  
CMD /usr/bin/kronos_api_crud  

