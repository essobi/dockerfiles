FROM node:wheezy  
  
EXPOSE 80  
# Download packages  
RUN apt-get update && apt-get install -y nginx \  
ruby \  
ruby-dev \  
build-essential \  
rubygems  
RUN npm install -g bower grunt-cli  
RUN gem install sass  
RUN gem install compass  
  
CMD ["nginx", "-g", "daemon off;"]  

