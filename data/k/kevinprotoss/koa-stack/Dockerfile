# DOCKER-VERSION ~1.1.0  
FROM ubuntu:14.04  
MAINTAINER Junxiang Wei <junxiang.wei@nodeunify.com>  
  
RUN apt-get update  
RUN apt-get install -y build-essential libssl-dev git curl  
  
RUN git clone https://github.com/creationix/nvm.git  
  
ENV NODE_VERSION v0.11.13  
RUN echo 'source /nvm/nvm.sh && nvm install ${NODE_VERSION}' | bash -l  
ENV PATH /nvm/${NODE_VERSION}/bin:${PATH}  
  
COPY . .  
  
RUN npm install  
  
EXPOSE 3000  
CMD ["npm", "start"]

