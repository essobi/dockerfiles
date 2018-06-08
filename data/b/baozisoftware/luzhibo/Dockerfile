#Base image  
FROM ubuntu:16.04  
MAINTAINER Baozisoftware Diklic "https://github.com/Baozisoftware"  
ENV PORT 12216  
#Install FFMpeg  
RUN apt-get update  
RUN apt-get install -y ffmpeg  
  
#Download luzhibo  
ADD
https://github.com/Baozisoftware/luzhibo/releases/download/latest/luzhibo_linux_amd64
/  
RUN chmod +x luzhibo_linux_amd64  
  
#Other  
EXPOSE $PORT  
CMD /luzhibo_linux_amd64 -port $PORT  

