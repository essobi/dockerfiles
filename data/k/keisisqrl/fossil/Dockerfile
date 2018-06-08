FROM alpine:3.6  
ENV USERNAME admin  
ENV FOSSIL_VERSION 2.4  
COPY runserver.sh /usr/local/bin/runserver.sh  
  
RUN apk add --no-cache curl \  
&& curl -fsSLo /tmp/fossil.tar.gz https://www.fossil-
scm.org/index.html/uv/fossil-linux-x64-$FOSSIL_VERSION.tar.gz \  
&& tar xf /tmp/fossil.tar.gz -C /usr/local/bin \  
&& rm /tmp/fossil.tar.gz \  
&& mkdir /fossils \  
&& chmod +x /usr/local/bin/runserver.sh \  
&& apk del --purge --no-cache curl \  
&& rm -f /var/cache/apk/*  
  
VOLUME ["/fossils"]  
  
WORKDIR "/fossils"  
  
EXPOSE 8080  
CMD ["/usr/local/bin/runserver.sh"]  

