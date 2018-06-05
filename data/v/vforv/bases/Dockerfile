FROM mhart/alpine-node:6.9.4  
RUN apk add --no-cache make gcc g++ python git iputils drill net-tools bash  
  
# Create app directory  
RUN mkdir -p /home/app  
RUN mkdir -p /home/app/test  
RUN mkdir -p /home/app/bases-service  
WORKDIR /home/app  
  
# Install app dependencies  
COPY package.json /home/app/bases-service  
RUN cd bases-service && npm install;  
  
# Bundle app source  
COPY . /home/app/bases-service  
  
EXPOSE 39999  
CMD cd bases-service ; npm start

