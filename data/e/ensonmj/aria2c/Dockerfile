FROM alpine:latest  
  
MAINTAINER ensonmj <ensonmj@gmail.com>  
  
WORKDIR /root  
  
RUN apk add --no-cache aria2 && \  
apk add --no-cache tzdata  
  
# user can add aria2.conf in /root/.aria2 to override this default conf  
COPY files/aria2.conf .config/aria2/aria2.conf  
COPY files/start.sh start.sh  
COPY files/on-complete.sh on-complete.sh  
  
ENV TZ="Asia/Shanghai" SECRET="" EXTERNAL_IP=""  
# 1) the folder to store downloadef files  
# 2) user should make their own session.dat file for persistence  
VOLUME ["/root/Downloads", "/root/.aria2"]  
  
EXPOSE 6800 16969 16969/udp  
  
CMD ["./start.sh"]  

