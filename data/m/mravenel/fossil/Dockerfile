FROM alpine:3.5  
ENV USERNAME admin  
ENV FOSSIL_VERSION 2.0  
COPY runserver.sh /usr/local/bin/runserver.sh  
  
RUN addgroup -Sg 400 fossil \  
&& adduser -Su 400 -G fossil fossil \  
&& apk add --no-cache curl \  
&& curl -fsSLo /tmp/fossil.tar.gz https://www.fossil-
scm.org/index.html/uv/download/fossil-linux-x64-$FOSSIL_VERSION.tar.gz \  
&& tar xf /tmp/fossil.tar.gz -C /usr/local/bin \  
&& rm /tmp/fossil.tar.gz \  
&& mkdir /data \  
&& chown -R fossil:fossil /data \  
&& chmod +x /usr/local/bin/runserver.sh \  
&& apk del --purge --no-cache curl \  
&& rm -f /var/cache/apk/*  
  
VOLUME ["/data"]  
  
WORKDIR "/data"  
  
EXPOSE 9000  
USER fossil  
  
CMD ["/usr/local/bin/runserver.sh"]  

