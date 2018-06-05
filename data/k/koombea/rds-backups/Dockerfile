FROM alpine:3.5  
LABEL mantainer="Juan Jaramillo <juan.jaramillo@koombea.com>"  
  
RUN ln -sf /usr/share/zoneinfo/America/Bogota /etc/localtime && \  
apk add --no-cache tzdata mysql-client postgresql=9.6.6-r0 bash=4.3.46-r5 tree
python py-pip && \  
pip install awscli  
  
ADD entrypoint /entrypoint  
WORKDIR /usr/src/app  
RUN mkdir backup/  
  
ENTRYPOINT ["/entrypoint"]  
  
CMD ["postgres"]  

