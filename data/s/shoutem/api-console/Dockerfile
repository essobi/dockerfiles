# Pull base image  
FROM nepalez/ruby  
MAINTAINER Kristijan Rebernisak <kristijan@shoutem.com>  
  
# Install packages  
RUN apt-get update && apt-get install -y git nodejs-legacy npm wget  
  
RUN wget -O api-console.tar.gz https://github.com/mulesoft/api-
console/archive/2.0.2.tar.gz  
RUN tar -xvzf api-console.tar.gz  
RUN rm api-console.tar.gz  
  
WORKDIR api-console-2.0.2  
# Install SASS, Bower & Grunt  
RUN gem install sass  
RUN npm install --silent -g bower grunt-cli  
  
RUN npm install --silent  
RUN bower install --allow-root  
  
# Copy the RAML specification to the container  
COPY ./shoutem /app/api-console-2.0.2/src/assets/shoutem  
COPY ./lightspeed /app/api-console-2.0.2/src/assets/lightspeed  
  
# Exposing port 9000 because this is the port api-console server uses  
EXPOSE 9000  
CMD [ "grunt", "--force"]  

