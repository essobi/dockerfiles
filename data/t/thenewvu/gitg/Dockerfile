FROM thenewvu/ubuntu-14.04  
MAINTAINER Vu Le "thenewvu@gmail.com"  
RUN sudo add-apt-repository ppa:gnome3-team/gnome3-staging && \  
sudo apt-get update && \  
sudo apt-get install -y gitg gir1.2-peas-1.0  
  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data/projects  
ENTRYPOINT ["/usr/bin/gitg"]  

