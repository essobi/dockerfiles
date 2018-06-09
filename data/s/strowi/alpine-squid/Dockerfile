FROM alpine:latest  
MAINTAINER Roman v. Gemmeren <strowi@hasnoname.de>  
  
RUN apk --update --no-cache add acf-squid \  
&& rm -fr /var/cache/squid \  
&& ln -sf /data /var/cache/squid \  
&& rm -fr /var/cache/apk/* \  
/tmp/* \  
/root/.cache \  
/root/.cached  
  
ADD src/ /  
  
EXPOSE 3128  
VOLUME ["/data"]  
  
CMD ["/docker-entrypoint.sh"]  

