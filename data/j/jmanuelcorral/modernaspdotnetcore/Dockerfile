FROM microsoft/aspnetcore-build:1.1-projectjson  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
RUN rm /usr/local/bin/bower  
RUN rm /usr/local/bin/gulp  
RUN rm /usr/local/bin/node  
RUN rm /usr/local/bin/nodejs  
RUN apt-get update  
RUN apt-get install -y apt-utils  
RUN apt-get install -y build-essential  
RUN curl -o- https://deb.nodesource.com/setup_7.x | bash  
RUN apt-get install -y nodejs  
RUN npm install -g webpack  
RUN npm install -g karma  
RUN npm install -g phantomjs

