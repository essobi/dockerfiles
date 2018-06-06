FROM debian:jessie  
  
RUN apt-get update && \  
apt-get upgrade -q -y && \  
apt-get install -q -y --no-install-recommends cowsay  
  
ENTRYPOINT ["/usr/games/cowthink"]  
  
CMD ["What is all the buzz about?"]  

