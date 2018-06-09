FROM node:carbon  
  
# cltl/StoryTeller  
RUN mkdir -p /src/app  
COPY . /src/app  
  
WORKDIR /src/app  
RUN yarn install  
RUN npm run build  
RUN yarn global add http-server  
  
EXPOSE 9001  
CMD ["http-server", "dist", "-p 9001"]  

