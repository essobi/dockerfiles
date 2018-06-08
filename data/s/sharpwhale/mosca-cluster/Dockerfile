# node image  
FROM node:8.2.1  
# docker mantainer  
# MAINTAINER reggie  
#RUN git clone https://github.com/mcollina/mosca.git  
#WORKDIR ./mosca  
# install all needed packages  
#RUN npm install  
RUN npm install redis --save && npm install mosca --save  
  
# add the files to load  
ADD ./broker.js .  
  
# expose port  
EXPOSE 1883  
# execute app.js  
ENTRYPOINT ["node", "broker.js"]

