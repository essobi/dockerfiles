# base image  
FROM node:8  
ARG UNAME=pizza  
ARG UID=1000  
ARG GID=1000  
RUN userdel node  
RUN groupadd -g $GID $UNAME  
RUN useradd -m -u $UID -g $GID -s /bin/bash $UNAME  
  
# add `/usr/src/app/node_modules/.bin` to $PATH  
ENV PATH /usr/src/app/node_modules/.bin:$PATH  
  
# install and cache react-scripts globally  
RUN npm install react-scripts@1.1.1 -g \  
&& npm cache clean --force  
  
# set working directory  
WORKDIR /usr/src/app  
RUN mkdir /usr/src/app/stats  
RUN mkdir /usr/src/app/dist  
RUN chown -R $UNAME:$UNAME /usr/src/app && chmod -R 775 /usr/src/app  
  
# Don't run stuff as root  
USER $UNAME  
  
# install app dependencies  
RUN npm -v  
COPY package.json /usr/src/app/package.json  
RUN npm install \  
&& npm cache clean --force  
  
# start app  
CMD ["npm", "start"]  

