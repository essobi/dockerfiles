FROM ubuntu:15.10  
MAINTAINER TrueAccord  
  
RUN apt-get update && apt-get install -y unzip  
  
ADD https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
ngrok.zip  
  
RUN unzip ngrok.zip -d /bin && rm -f ngrok.zip && touch /.ngrok  
  

