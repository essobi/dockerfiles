FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7  
#converting to nginx  
COPY ./app /app  
  
#Restore if logs aren't as expected  
#RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
# ln -sf /dev/stderr /var/log/nginx/error.log  
#update the image add rsyslog, git, and openrc  
RUN apk update  
RUN apk add --no-cache git  
  
#install youtube-dl  
RUN pip install --upgrade youtube_dl  
  
#pull the primary repo  
RUN git clone https://github.com/chewett/youtube-playlist-sync.git  
  
#Where shall I copy this to now?  
#COPY ./www /usr/html  
#CMD tail -f /dev/null  

