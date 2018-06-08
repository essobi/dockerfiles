FROM perl:latest  
LABEL maintainer "Roman Imankulov <roman.imankulov@gmail.com>"  
  
EXPOSE 4444  
RUN apt-get update && \  
apt-get install -y ucspi-tcp && \  
rm -rf /var/lib/apt/lists/*  
COPY FlameGraph /usr/src/FlameGraph  
WORKDIR /usr/src/FlameGraph  
CMD ["tcpserver", "0.0.0.0", "4444", "perl", "./flamegraph.pl"]  

