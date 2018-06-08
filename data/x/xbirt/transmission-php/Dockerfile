FROM linuxserver/transmission:latest  
RUN apk update && \  
apk add --no-cache php5 unrar && \  
rm -rf /var/cache/apk/* && \  
echo "* * * * * s6-setuidgid abc find /config -type f ! -perm -004 -exec chmod
a+r {} \;" > /etc/crontabs/root  

