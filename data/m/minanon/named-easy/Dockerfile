FROM alpine  
  
RUN apk update \  
&& apk add bind openssl  
  
COPY add_files/generator /generator  
COPY add_files/generator.sh /generator.sh  
COPY add_files/entrypoint.sh /entrypoint.sh  
  
EXPOSE 53/tcp 53/udp  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

