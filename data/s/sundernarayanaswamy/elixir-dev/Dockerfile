FROM elixir  
  
MAINTAINER sunder.narayanaswamy@gmail.com  
  
# Install node required for Phoenix framework  
RUN apt-get update && apt-get install -y \  
inotify-tools emacs git silversearcher-ag build-essential tree  
  
RUN bash -c "curl -sL https://deb.nodesource.com/setup_6.x | bash -"  
  
RUN apt-get install -y nodejs  
  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
apt-get -y autoclean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4000  
WORKDIR /root  
  
CMD /bin/bash  
# tail -f /dev/null  

