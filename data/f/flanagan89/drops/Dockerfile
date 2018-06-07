FROM node:9-alpine  
  
LABEL "author"="Rian Finnegan"  
  
# install Hexo  
RUN npm install hexo-cli -g  
  
# set workdir  
WORKDIR /public  
  
# copy context into workdir  
COPY . .  
  
# install dependency  
RUN yarn install  
  
# generate static files  
RUN hexo generate  
  
# hexo default port  
EXPOSE 4000  
# start the built in hexo server, prod mode, serves static files  
CMD ["hexo", "server", "-s"]

