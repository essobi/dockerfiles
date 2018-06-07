FROM node:8.9-wheezy  
  
RUN apt-get update  
RUN apt-get install -y rsync  
  
  
RUN npm install -g \  
gulp-cli \  
grunt-cli \  
bower \  
markdown-styles \  
yarn \  
less \  
coffeescript  
  
# Temp fix? https://github.com/npm/npm/issues/17851  
RUN yarn global add node-sass  
# Heheheeheheh, sorry about this.  
# TODO: Use sudo usermod or something to fix UID problems  
RUN adduser --disabled-password --gecos "" \--home /home/node node1  
RUN adduser --disabled-password --gecos "" \--home /home/node node2  
RUN adduser --disabled-password --gecos "" \--home /home/node node3  
RUN adduser --disabled-password --gecos "" \--home /home/node node4  
RUN adduser --disabled-password --gecos "" \--home /home/node node5  
RUN adduser --disabled-password --gecos "" \--home /home/node node6  
RUN adduser --disabled-password --gecos "" \--home /home/node node7  
RUN adduser --disabled-password --gecos "" \--home /home/node node8  
RUN adduser --disabled-password --gecos "" \--home /home/node node9  
  
CMD ["/usr/local/bin/npm"]  

