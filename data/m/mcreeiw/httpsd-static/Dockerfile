FROM alpine:latest  
LABEL maintainer="Erno Rigo <erno@rigo.info>"  
LABEL description="Simple dockerfile based on alpine to provide static web
content via https \  
self signed certificates are generated automatically. \  
The image utilizes openssl and mini_httpd to do the heavy lifting."  
COPY public /public  
COPY work /work  
RUN apk update && \  
apk add openssl mini_httpd && \  
chmod +x /work/entrypoint.sh  
#CMD mini_httpd -d /public -S -E /cert/site.keycrt -p 443 -D -u root  
#CMD mini_httpd -d /public -p 80 -D -u root  
#ENTRYPOINT mini_httpd -d /public -S -E /cert/site.keycrt -p 443 -D -u root  
ENTRYPOINT ["/work/entrypoint.sh"]  
#CMD ["mini_httpd", "-d", "/public", "-S", "-E", "/cert/site.keycrt", "-p",
"443", "-D", "-u", "root"]  
CMD ["mini_httpd", "-d", "/public", "-D", "-S", "-E", "/certs/all.pem"]  

