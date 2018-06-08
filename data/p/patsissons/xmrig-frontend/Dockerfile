FROM alpine  
  
ENV HTDOCS_PATH /var/www/localhost/htdocs  
ENV REPO_URI https://github.com/dunklesToast/XMRigFrontend.git  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache lighttpd git && \  
rm -rf /var/cache/apk/*  
  
COPY root /  
  
EXPOSE 80  
CMD [ "/bin/sh", "/scripts/entrypoint.sh" ]  

