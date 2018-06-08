FROM node:5.0-slim  
  
RUN wget -O /wait-for-it.sh https://raw.githubusercontent.com/iturgeon/wait-
for-it/8f52a814ef0cc70820b87fbf888273f3aa7f5a9b/wait-for-it.sh \  
&& chmod +x /wait-for-it.sh  
  
COPY . /data/  
WORKDIR /data/  
RUN npm install  
ENV PATH=/data/node_modules/.bin:$PATH  
CMD knex migrate:latest  

