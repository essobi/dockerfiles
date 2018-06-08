FROM circleci/python:3.6  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main"
\  
| sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list  
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends
mongodb-org-server && mongod --version  

