FROM alpine:3.6  
ARG PHP_PACKAGE  
  
  
RUN : \  
&& apk --update --no-cache add "${PHP_PACKAGE}" \  
&& mkdir -p /run/apache2 \  
&& ln -sfT /dev/stderr /var/log/apache2/error.log \  
&& ln -sfT /dev/stdout /var/log/apache2/access.log \  
&& :  
  
COPY root /  
  
FROM scratch  
COPY \--from=0 / /  
  
ENTRYPOINT ["image--entrypoint"]  
CMD ["image--start"]  

