FROM drush/drush:8  
# zip and nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -y nodejs zip  
  
# terminus  
RUN mkdir -p /root/terminus && mkdir -p /root/.terminus/cache && mkdir -p
/root/.terminus/plugins  
WORKDIR /root/terminus  
RUN curl -O https://raw.githubusercontent.com/pantheon-systems/terminus-
installer/master/builds/installer.phar && php installer.phar install  
  
ENV PATH="/root/terminus/vendor/bin:${PATH}"  
# terminus plugins  
RUN curl https://github.com/pantheon-systems/terminus-mass-
update/archive/v1.0.0.tar.gz -L | tar -C ~/.terminus/plugins -xvz  
  
WORKDIR /usr/src/app  
  
ENTRYPOINT []  
CMD npm install & npm start

