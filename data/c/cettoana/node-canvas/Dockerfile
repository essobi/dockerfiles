FROM nodesource/trusty:6.3.1  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update -qq  
  
RUN apt-get install -qy libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev
build-essential g++ yarn  

