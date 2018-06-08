FROM ruby:2.3-slim  
MAINTAINER supermomonga  
  
RUN apt-get update\  
&& apt-get install -y librtmp-dev git build-essential\  
&& rm -rf /var/lib/apt/lists/**  
  
WORKDIR /app  
RUN git clone https://github.com/kbinani/nicolive-dl.git /app\  
&& git clone https://github.com/kbinani/rtmpdump-nico-live.git
/app/ext/rtmpdump\  
&& make  
  
VOLUME /data  
  
ENTRYPOINT ["/app/bin/nicolive-dl"]  
CMD ["-h"]  
  

