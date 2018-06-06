FROM node  
MAINTAINER Pablo Castro <castrinho8@gmail.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main"
| tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
  
RUN apt-get -y update && apt-get install -y nodejs && apt-get install -y npm
&& apt-get install -y mongodb-org  
RUN mkdir -p /usr/tickets-core  
COPY . /usr/tickets-core  
  
WORKDIR /usr/tickets-core  
RUN npm install  
  
EXPOSE 3000  
CMD service mongod start && npm run start  

