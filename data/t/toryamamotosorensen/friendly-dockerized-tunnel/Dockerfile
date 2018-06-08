FROM alpine:3.6  
LABEL maintainer "https://github.com/tbys"  
  
RUN apk add --no-cache autossh  
RUN mkdir -p ~/.ssh  
RUN echo "ServerAliveInterval=180" >> ~/.ssh/config  
  
COPY ./run.sh ./run.sh  
RUN chmod 755 ./run.sh  
  
CMD ["./run.sh"]  

