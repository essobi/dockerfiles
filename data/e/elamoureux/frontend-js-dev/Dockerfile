# Build from Ubuntu stable  
FROM ubuntu:14.04  
# Fetch Node and install it  
RUN apt-get update && apt-get -y install \  
curl \  
bash \  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get -y install \  
nodejs \  
npm  
  
# Install dev tools with npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g \  
yo \  
bower \  
grunt-cli \  
gulp \  
generator-gulp-angular \  
generator-gulp-angular-subtask  
  
# Additionnal config for yeoman  
RUN adduser --disabled-password --gecos "" yeoman; \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
ENV HOME /home/yeoman  
USER yeoman  
  
# Expose default gulp port  
EXPOSE 3000  
# Run with bash  
WORKDIR /dev-env  
CMD ["/bin/bash"]

