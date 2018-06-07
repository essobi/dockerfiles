FROM ethereum/client-go:stable  
  
#RUN apk add --no-cache wget ca-certificates && wget --no-check-certificate
https://gethstore.blob.core.windows.net/builds/geth-linux-
amd64-1.7.3-4bb3c89d.tar.gz && tar zxvf *tar.gz && mv geth-linux-
amd64-1.7.3-4bb3c89d/geth /usr/bin && rm -rf geth* && apk del wget ca-
certificates  
#RUN chmod -R 777 /usr/bin/geth  
#ENTRYPOINT /usr/local/bin/geth  
RUN apk add --no-cache nginx  
  
RUN apk add --no-cache bash  
  
RUN sed -i "s#pcre_jit on;#pid /run/nginx.pid;#g" /etc/nginx/nginx.conf  
  
ENTRYPOINT []  

