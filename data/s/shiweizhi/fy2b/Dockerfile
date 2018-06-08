FROM alpine:latest  
  
RUN apk update;apk add python3 wget uwsgi ca-certificates ffmpeg uwsgi-python3  
RUN pip3 install requests flask youtube-dl  
  
WORKDIR /root  
RUN wget "https://github.com/shiwzhi/fy2b/archive/master.zip";unzip
master.zip;mv fy2b-master fy2b;chmod o+x /root  
  
EXPOSE 3010  
ENTRYPOINT ["uwsgi", "--ini", "/root/fy2b/fy2b.ini"]

