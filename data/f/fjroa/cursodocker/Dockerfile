FROM node:latest  
  
MAINTAINER BTree Press  
  
  
  
  
COPY . /var/www  
WORKDIR /var/www  
  
RUN npm install  
  
EXPOSE 8080  
ENTRYPOINT ["npm", "start"]  
  
# To build:  
# docker build -f docker-node-btree.dockerfile --tag btree/node ../  
# docker build -f docker-node-btree.dockerfile --tag btree/dfd-node ../  
# To run:  
# docker run -d -p 8080:8080 -v $(PWD):/var/www/btree/ -w /var/www/btree
btree/btree-node  
# docker run -d -p 8080:8080 --name dfd-node btree/dfd-node  
#step 4  
# Seed or add pets the petDB the database in mongo  
# - here we are demoing the using the *exec* command to show how to execute a
command in a running container.  
# - alternatively you can ssh in the container and do the same thing but this
ay is much simpler.  
#command:  
# docker exec nodeapp node dbSeeder.js  

