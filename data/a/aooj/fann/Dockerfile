# docker fann  
#  
# VERSION 1.2  
#  
# use cat app.js | docker run -i aooj/fann node  
#  
FROM aooj/base:latest  
MAINTAINER AooJ <aoj@n13.cz>  
  
  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y libfann2 libfann-dev pkg-config libglib2.0-dev make gcc
g++ nodejs && apt-get clean  
  
RUN echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >>
/root/.bash_profile  
  
RUN cd / && npm install fann  
  

