FROM debian  
MAINTAINER Josh Wheeler <mantlepro@gmail.com>  
RUN apt-get update && apt-get install -y mp3cd  
ENTRYPOINT mp3cd  
CMD -T -E /mnt/*  

