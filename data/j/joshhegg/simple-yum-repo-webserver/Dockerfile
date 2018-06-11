FROM library/nginx:stable  
RUN apt-get update && apt-get install -y createrepo  
COPY recursively-createrepo.sh /usr/bin/recursively-createrepo.sh  
RUN chmod +x /usr/bin/recursively-createrepo.sh  
VOLUME /usr/share/nginx/html  
EXPOSE 80  
CMD /bin/bash -c "/usr/bin/recursively-createrepo.sh && echo 'Starting
webserver.' && nginx -g 'daemon off;'"  
  

