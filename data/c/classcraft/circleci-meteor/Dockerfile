FROM circleci/node:8.11-browsers  
  
RUN curl "https://install.meteor.com/?release=1.6.1.1" | /bin/sh  
RUN echo "Meteor version:";meteor --version;which meteor;echo "Meteor node
version:";meteor node -v;echo "Meteor npm version:";meteor npm -v;echo "Java
version:";java -version  
  
USER root  
RUN git clone https://www.agwa.name/git/git-crypt.git  
RUN cd git-crypt && make && make install  
  
USER node  
ENV NPM_CONFIG_PREFIX=~/.npm  
RUN npm install --global chimp  
  
USER root  
RUN ln -s /home/node/.npm/bin/chimp /usr/local/bin/  
  
USER circleci  

