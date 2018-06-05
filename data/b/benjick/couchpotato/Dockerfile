FROM gliderlabs/alpine:3.3  
RUN apk add --no-cache \  
python \  
py-lxml \  
curl  
  
EXPOSE 5050  
RUN mkdir /opt && curl -o /opt/cp.tar.gz -SL
https://github.com/RuudBurger/CouchPotatoServer/archive/build/3.0.1.tar.gz \  
&& cd /opt && tar -xzf cp.tar.gz && rm cp.tar.gz && ls -la CouchPotatoServer-
build-3.0.1  
  
RUN apk del curl  
#CMD  
CMD ["python", "/opt/CouchPotatoServer-build-3.0.1/CouchPotato.py"]  

