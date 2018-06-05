FROM bradleybossard/docker-node-devbox  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
  
RUN mkdir -p /data/db  
  
RUN apt-get install -y python \  
sudo \  
ruby \  
mongodb \  
build-essential  
  
RUN gem install sass  
  
RUN npm install -g yo \  
generator-angular-fullstack \  
generator-meanjs  
  
# Add a yeoman user because grunt doesn't like being root  
RUN adduser --disabled-password --gecos "" yeoman && \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# set HOME so 'npm install' and 'bower install' don't write to /  
ENV HOME /home/yeoman  
  
# Always run as the yeoman user  
USER yeoman  
  
WORKDIR /home/yeoman  
  
EXPOSE 3000  
ENV LANG en_US.UTF-8  
CMD /bin/bash  

