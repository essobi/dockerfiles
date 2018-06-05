FROM ruby:2.3.0  
# Install nodejs  
RUN apt-get update  
RUN apt-get --assume-yes --force-yes install nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install bower  
RUN npm install -g bower  
  
# Install CloudFoundry  
RUN curl -L
'https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.15.0&source=github-
rel' > /tmp/cf.tar.gz  
RUN tar -xzvf /tmp/cf.tar.gz  
RUN mv cf /usr/local/bin/cf  

