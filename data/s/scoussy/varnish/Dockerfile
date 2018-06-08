FROM alpine  
  
RUN apk add -U bash varnish  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
ADD ./varnishreload.sh /usr/sbin/varnishreload  
RUN chmod 755 /usr/sbin/varnishreload  
  
COPY src /src  
RUN chmod 755 /src/make.sh  
RUN /src/make.sh  
RUN rm -Rf /src  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
ENTRYPOINT [ "/entrypoint.sh" ]  
  
EXPOSE 80  

