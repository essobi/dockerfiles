FROM quitoque/ubuntu16-04-php7-apache2  
  
MAINTAINER Rémi Chomat <remi@quitoque.fr>  
  
RUN apt-get update && apt-get -qq -y install nodejs npm && \  
mkdir /home/quitoque/.npm && \  
chown -R quitoque:quitoque /home/quitoque/.npm && \  
npm cache clean && npm update -g && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
apt-get -qq -y autoremove && apt-get -qq -y autoclean && \  
apt-get -qq -y clean && rm -rf /var/lib/apt/lists/*  

