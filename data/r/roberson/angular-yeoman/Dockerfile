FROM node:5-slim  
  
MAINTAINER Roberson Faria roberson.faria@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -yq update && \  
apt-get -yq install git net-tools sudo bzip2 ruby-compass &&\  
apt-get clean  
  
RUN npm install -g --silent yo@1.8.4 bower@1.7.9 gulp@3.9.1 gulp-cli@1.2.1  
  
# Add a yeoman user because grunt doesn't like being root  
RUN adduser --disabled-password --gecos "" yeoman && \  
echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# Expose the port  
EXPOSE 9000 35729  
# set HOME so 'npm install' and 'bower install' don't write to /  
ENV HOME /home/yeoman  
  
ENV LANG en_US.UTF-8  
RUN mkdir /src && chown yeoman:yeoman /src  
WORKDIR /src  
  
ADD set_env.sh /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/set_env.sh  
ENTRYPOINT ["set_env.sh"]  
  
# Always run as the yeoman user  
USER yeoman  
  
RUN sudo npm install -g --silent grunt-cli@1.2.0 \  
generator-angular@0.15.1 generator-karma@2.0.0 grunt-bower-install@1.6.0
generator-karma-require@1.1.0 generator-angular-require@3.5.0  
  
CMD ["grunt", "serve"]  

