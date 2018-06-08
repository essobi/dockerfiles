FROM node:0.10  
RUN apt-get update -qq && apt-get install -y build-essential  
RUN apt-get install -y ruby  
RUN gem install sass  
  
RUN mkdir /src  
  
RUN npm install gulp -g  
  
WORKDIR /src  
ADD app /src/  
RUN npm install  
RUN gulp buildBundle  
  
EXPOSE 3000  
CMD node app.js  

