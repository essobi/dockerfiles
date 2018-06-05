FROM ruby:2.2.0  
RUN apt-get update && apt-get install -y \  
curl \  
gzip \  
jpegoptim \  
optipng \  
nodejs \  
npm \  
python \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN \  
npm install uglify-js@2.4.16 cssmin@0.4.3 -g  
  
RUN \  
gem install aws-sdk --version 2.0.28  
  
ENV STORAGE_PATH /docker  
  
COPY assets-deploy.rb /usr/local/bin/assets-deploy  
RUN chmod +x /usr/local/bin/assets-deploy  
  
CMD assets-deploy /usr/src/app/public  

