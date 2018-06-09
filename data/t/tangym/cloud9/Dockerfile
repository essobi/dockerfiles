FROM node  
MAINTAINER tym  
  
RUN apt-get update  
RUN apt-get install -y git tmux curl wget make g++ python  
RUN git clone https://github.com/c9/core.git /c9sdk  
RUN /c9sdk/scripts/install-sdk.sh  
  
# pre-install  
RUN apt-get install -y nginx  
# pre-install end  
VOLUME /home/  
WORKDIR /home/  
  
EXPOSE 8000  
ENV USERNAME your_username  
ENV PASSWORD password  
ENTRYPOINT ["sh", "-c", "node /home/c9sdk/server.js -p 8000 -l 0.0.0.0 -a
$USERNAME:$PASSWORD"]  

