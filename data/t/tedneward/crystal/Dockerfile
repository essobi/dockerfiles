FROM ubuntu  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN apt-get update && \  
apt-get install -y curl apt-transport-https && \  
curl https://dist.crystal-lang.org/apt/setup.sh | bash && \  
apt-get install -y build-essential crystal  
  
RUN groupadd --gid 1000 crystal \  
&& useradd --uid 1000 --gid crystal --shell /bin/bash --create-home crystal \  
&& chown -R crystal:crystal /usr/local  
  
USER crystal  
WORKDIR /home/crystal  
  
ENTRYPOINT ["/bin/bash"]  

