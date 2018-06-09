FROM codenvy/shellinabox  
  
RUN sudo apt-get update && \  
sudo apt-get upgrade -y && \  
sudo apt-get install -y ruby ruby-dev patch nodejs python locales && \  
sudo gem install github-pages  
RUN sudo dpkg-reconfigure locales && \  
sudo locale-gen C.UTF-8 && \  
sudo /usr/sbin/update-locale LANG=C.UTF-8  
  
  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
  
EXPOSE 4000  
ENV CODENVY_APP_PORT_4000_HTTP 4000  

