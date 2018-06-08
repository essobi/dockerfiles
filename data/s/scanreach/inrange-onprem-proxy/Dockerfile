FROM nginx  
RUN apt-get update && apt-get -y install inotify-tools && rm -rf
/var/lib/apt/lists/*  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY location.inrange /etc/nginx/location.inrange  
COPY runnginx.sh /usr/runnginx.sh  
RUN chmod +x /usr/runnginx.sh  
CMD /usr/runnginx.sh

