FROM node:8  
MAINTAINER Matt Malone <swapthatspoon@gmail.com>  
  
RUN mkdir -p /app  
WORKDIR /app  
  
# yarn.lock & package.json are added separately from the app to speed up build
time if those haven't changed.  
RUN npm install yarn  
COPY yarn.lock /app/  
COPY package.json /app/  
RUN yarn install  
  
ARG GIT_SHA1  
RUN echo "export GIT_SHA1=$GIT_SHA1" >> /root/.bashrc  
COPY . /app/  
  
ENTRYPOINT ["/app/container/docker-entrypoint.sh"]  
CMD ["run"]  
EXPOSE 3000  

