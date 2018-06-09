FROM alpine:3.4  
MAINTAINER towb <me@towb.xyz>  
  
ENV ZNCDATA /znc-data  
ENV ZNCMOD /znc-data/modules  
  
RUN apk add --update \  
znc ca-certificates su-exec \  
&& rm -rf /var/cache/apk/* \  
&& mkdir "$ZNCDATA" && chown znc "$ZNCDATA"  
  
COPY docker-entrypoint.sh /  
COPY znc.conf.default /  
  
VOLUME $ZNCDATA  
  
EXPOSE 6667  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["znc"]  

