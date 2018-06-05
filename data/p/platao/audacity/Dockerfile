# Run container in Desktop:  
  
# xhost +local:docker;  
  
# docker run --rm --name audacity \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v $HOME/Desktop:/home \  
# -e DISPLAY \  
# platao/audacity;  
  
# xhost -local:docker;  
  
FROM debian:stretch  
  
RUN apt-get update && apt-get install -y \  
audacity \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home  
  
ENTRYPOINT ["audacity"]  

