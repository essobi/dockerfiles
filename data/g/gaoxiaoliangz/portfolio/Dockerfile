FROM ruby:2.1  
# RUN cd ~  
RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh  
RUN bash nodesource_setup.sh  
RUN apt-get install nodejs  
RUN npm install -g yarn  
  
RUN node -v  
RUN npm -v  
RUN yarn -v  
  
RUN LC_ALL=en_US.UTF-8  
RUN LANG=en_US.UTF-8  
  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
RUN gem install sass  
RUN npm install  
RUN npm run build  
  
CMD [ "node", "./src/server" ]  

