FROM debian:stretch-slim  
  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" TERM="xterm"  
WORKDIR /usr/bin  
  
ADD https://r.mistserver.org/dl/mistserver_64V2.8.2.tar.gz /usr/bin  
  
RUN tar -zxvf mistserver_64V2.8.2.tar.gz -C /usr/bin && \  
rm -f mistserver_64V2.8.2.tar.gz  
  
CMD ["/usr/bin/MistController"]  
  
WORKDIR /videos  
  
VOLUME ["/videos"]  
  
EXPOSE 4242 8080 1935 554  

