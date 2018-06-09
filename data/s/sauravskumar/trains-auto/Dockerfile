FROM node:6  
  
#RUN npm install -g yarn  
#RUN npm install -g phantomjs  
#  
#RUN mkdir -p /usr/src/app  
#  
#WORKDIR /usr/src/app  
#  
#COPY package.json /usr/src/app/  
#  
#  
##RUN yarn global add phantomjs  
#  
##RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg  
##RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
##RUN apt-get update  
##RUN apt-get install yarn  
#  
#COPY . /usr/src/app  
#  
#RUN yarn install  
#  
#ENV docker true  
#  
#RUN npm run build  
#  
#CMD ["/bin/bash"]  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
  
RUN npm install  
  
ENV docker true  
  
COPY . /usr/src/app  
  
RUN npm run build  
  
RUN npm cache clean  
  
CMD ["/bin/bash"]  

