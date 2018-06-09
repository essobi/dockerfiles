FROM ubuntu  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get update  
RUN apt-get install -y mongodb-org  
RUN service mongod start  
RUN apt-get install -y nodejs  
RUN apt-get install npm git git-core -y  
ADD test /home/test  
COPY package.json /home/  
EXPOSE 3000  
RUN cd /home; npm install; npm install -g mocha;npm install mocha chai
supertest  
CMD ["nohup","/usr/bin/nodejs", "ugr-transparente-
servidor/lanzarTransparente.sh"]  

