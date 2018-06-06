FROM alpine:3.6  
MAINTAINER Joe Groocock <frebib@gmail.com>  
  
ADD newcert /usr/bin  
  
RUN apk --no-cache add tini docker certbot openssl && \  
# Remove large unused docker binaries  
rm -f /usr/bin/docker-* /usr/bin/dockerd && \  
echo '0 6 * * * date && certbot renew --agree-tos --preferred-challenges
http,dns --post-hook "$POST_HOOK" # Renew certificates at 6am' >
/etc/crontabs/root  
  
ENV POST_HOOK="docker restart nginx"  
VOLUME /var/run/docker.sock  
  
ENTRYPOINT [ "/sbin/tini", "--" ]  
CMD [ "/usr/sbin/crond", "-f", "-l", "6", "-L", "/dev/stdout" ]  
  

