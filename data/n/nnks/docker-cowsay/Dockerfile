FROM debian  
  
MAINTAINER nnks <ntomoya@gmail.com>  
  
RUN apt-get update && apt-get install -y cowsay fortune  
COPY entrypoint.sh /  
  
ENTRYPOINT ["./entrypoint.sh"]  

