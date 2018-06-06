FROM ubuntu:latest  
  
RUN apt-get update -y && apt-get install -y \  
ffmpeg \  
libass-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /capture  
  
COPY addsubs.sh /usr/local/bin/  
RUN chmod ug+x /usr/local/bin/addsubs.sh  
ENTRYPOINT ["/usr/local/bin/addsubs.sh"]  
CMD ["help"]  

