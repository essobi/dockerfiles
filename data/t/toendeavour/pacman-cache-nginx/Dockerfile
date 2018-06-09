FROM nginx:alpine  
LABEL maintainer="Marc Mettke <marc@itmettke.de>"  
  
RUN apk --no-cache add bash && \  
rm /etc/nginx/conf.d/default.conf && \  
mkdir /cache && \  
chown nginx:nginx /cache  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
EXPOSE 80  
VOLUME /cache  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
HEALTHCHECK CMD /bin/ash -c "PID=\$(cat /var/run/nginx.pid) && [ -n
\"\${PID}\" -a -d \"/proc/\${PID}\" ] && exit 0 || exit 1"  

