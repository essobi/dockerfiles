FROM golang:1.8  
ENV BEEPING_VERSION="0.5.0"  
RUN curl -sSfL
"https://github.com/yanc0/beeping/releases/download/v$BEEPING_VERSION/beeping"
> /usr/bin/beeping && \  
chmod +x /usr/bin/beeping  
  
EXPOSE 8080  
ADD ./support_files/docker-startup.sh /docker-startup.sh  
RUN chmod +x /docker-startup.sh  
  
CMD ["/docker-startup.sh", "/usr/bin/beeping"]  

