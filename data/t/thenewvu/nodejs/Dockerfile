FROM thenewvu/ubuntu-14.04  
MAINTAINER Vu Le "thenewvu@gmail.com"  
# install node.js 5.x and needed packages  
RUN wget -qO- https://deb.nodesource.com/setup_5.x | sudo -E bash - && \  
sudo apt-get update && \  
sudo apt-get install -y git nodejs  
  
# setup prefix  
RUN npm config set prefix /home/vu/.npm  
ENV PATH $PATH:/home/vu/.npm/bin  
RUN sudo sh -c "echo 'export NODE_PATH="'$(npm root -g)'"' >>
/etc/profile.d/npm.sh"  
  
# clean up  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data/projects  
ENTRYPOINT ["/bin/bash"]  

