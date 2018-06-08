# docker build -t medialon/felix:0.1.27 .  
FROM node  
# RUN apk add --update nodejs  
# RUN apk add --no-cache bash  
#create an app directory  
RUN mkdir -p /apps  
WORKDIR /apps  
  
#npm install because of mem-watch  
COPY package.json /apps  
RUN npm install  
  
# Copy apps build in another folder  
RUN echo Copying apps  
COPY . /apps  
  
#expose the port  
EXPOSE 3000  
#start the app  
ENV NODE_ENV=development  
  
WORKDIR /apps  
  
# comment if need a console in the container  
CMD [ "node", "index.js" ]  
  
# uncomment if needs a console in the container  
#CMD [ "/bin/bash"]

