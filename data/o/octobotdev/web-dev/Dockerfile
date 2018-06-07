FROM node:latest  
MAINTAINER Juan Saavedra <jsaavedra@octobot.io>  
RUN apt-get update &&\  
apt-get install -y\  
ruby\  
rubygems\  
ruby-dev\  
python3\  
python3-pip &&\  
gem install sass &&\  
gem install compass  
VOLUME /usr/development/app  
WORKDIR /usr/development/app  
RUN npm install -g yo bower grunt-cli gulp-cli gulp grunt create-react-app  
EXPOSE 9000 3000 35729  
CMD ["gulp", "serve"]  

