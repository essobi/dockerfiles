FROM node:latest  
  
# cltl/StoryTeller  
RUN mkdir -p /src/app  
COPY . /src/app  
  
WORKDIR /src/app  
RUN npm install  
RUN npm install -g pushstate-server  
# RUN npm install -g typescript@2.0.10  
# RUN tsc --version  
RUN npm run build  
  
EXPOSE 9000  
CMD ["pushstate-server", "build"]  

