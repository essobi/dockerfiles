FROM thenewvu/oracle-jdk8  
MAINTAINER Vu Le "thenewvu@gmail.com"  
# install Smartgit  
RUN sudo add-apt-repository ppa:eugenesan/ppa && \  
sudo apt-get update && \  
sudo apt-get install -y --no-install-recommends libgtk2.0-0 libxext-dev
libxrender-dev libxtst-dev smartgit  
  
# clean up  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data/projects  
ENTRYPOINT ["/usr/bin/smartgit"]  

