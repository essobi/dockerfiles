FROM alpine:3.7  
MAINTAINER Sascha Marcel Schmidt <docker@saschaschmidt.net>  
  
RUN addgroup -g 666 -S headphones && \  
adduser -u 666 -D -S -G headphones headphones  
  
RUN apk --no-cache add git python  
RUN git clone \--depth 1 https://github.com/rembo10/headphones.git
/opt/headphones \  
&& chown -R headphones:headphones /opt/headphones  
  
WORKDIR "/opt/headphones"  
VOLUME ["/var/headphones", "/var/download"]  
EXPOSE 8181  
USER headphones  
  
COPY headphones.ini /opt/headphones/  
CMD ["/opt/headphones/Headphones.py"]  

