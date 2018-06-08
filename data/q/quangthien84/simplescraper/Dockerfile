FROM node:latest  
RUN mkdir /home/simplescraper  
COPY Code /home/simplescraper  
RUN cd /home/simplescraper;npm install -g bower gulp requirejs;npm install;
bower install --allow-root; gulp less; gulp build;  
RUN cd /home/simplescraper/build; npm install  
EXPOSE 8081  
WORKDIR /home/simplescraper/build  
CMD ["node", "server"]  
  

