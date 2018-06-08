# Dockerfile for lighttpd  
FROM alpine  
  
ENV LANG=en_US.UTF-8  
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/sti  
COPY ./.sti/bin/ /usr/libexec/sti  
  
RUN apk add --update --no-cache lighttpd lighttpd-mod_auth  
RUN rm -rf /var/cache/apk/*  
COPY etc/* /opt/app-root/etc/  
RUN mkdir -m 0770 -p /srv/www /opt/app-root/log/  
  
EXPOSE 8080  
EXPOSE 8081  
RUN chown -R 1001:1001 /srv/www  
RUN chown -R 1001:1001 /opt/app-root/etc  
USER 1001  
CMD ["echo", "This image is intended for use with s2i"]  

