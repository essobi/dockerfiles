FROM ubuntu:14.04  
# make sure apt is up to date  
RUN apt-get update  
  
# install nodejs, npm and memcached  
RUN apt-get install -y curl; curl -sL https://deb.nodesource.com/setup_0.12 |
sudo bash -; apt-get install -y nodejs; apt-get install -y memcached;  
  
# copy source file and run npm install to get all node modules  
COPY ./ /src  
  
# expose port container to localhost of docker  
EXPOSE 8081  
CMD ["nodejs", "/src/src/engine/Main.js"]  

