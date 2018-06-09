FROM thenewvu/oracle-jdk8  
MAINTAINER Vu Le "thenewvu@gmail.com"  
RUN wget -qO- https://deb.nodesource.com/setup_5.x | sudo -E bash - && \  
sudo apt-get install -y --no-install-recommends nodejs && \  
sudo apt-get install -y --no-install-recommends git && \  
sudo npm install -g react-native-cli && \  
npm config set registry registry=https://registry.npm.taobao.org  
  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/  
  
WORKDIR /data/projects  
ENTRYPOINT ["/bin/bash"]  

