FROM debian:jessie  
RUN apt-get update && apt-get install weex && apt-get clean && rm -rf
/var/lib/apt/lists/*  
COPY entrypoint /entrypoint  
ENTRYPOINT [ "/entrypoint" ]  

