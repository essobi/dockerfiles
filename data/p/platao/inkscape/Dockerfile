# Run container in Desktop:  
  
# xhost +local:docker;  
  
# docker run --rm --name inkscape \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v $HOME/Desktop:/home \  
# -e DISPLAY \  
# platao/inkscape;  
  
# xhost -local:docker;  
  
FROM debian:stretch  
  
RUN apt-get update && apt-get -y install \  
apt-utils \  
inkscape \  
fonts-liberation \  
fonts-font-awesome && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home  
  
ENTRYPOINT ["inkscape"]  

