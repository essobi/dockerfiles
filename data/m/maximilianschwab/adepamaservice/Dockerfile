FROM node:latest  
WORKDIR /service  
COPY . /service  
EXPOSE 10010  
RUN cd /service && npm install && npm install -g swagger  
CMD swagger project start

