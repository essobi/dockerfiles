FROM node:4-wheezy  
  
RUN useradd --user-group --create-home --shell /bin/false app &&\  
npm install --global npm@3.7.5 &&\  
npm install --global grunt-cli@1.2.0 &&\  
npm install --global bower@1.7.9 &&\  
npm install --global phantomjs-prebuilt@2.1.12  
  
# Install gem sass for grunt-contrib-sass  
RUN apt-get update -qq && apt-get install -y build-essential ruby graphviz
openjdk-7-jre zlib1g-dev libreadline-dev libssl-dev libcurl4-openssl-dev &&
gem install sass  
# zlib1g-dev libreadline-dev libssl-dev libcurl4-openssl-dev  
# RUN gem install sass  
ENV HOME=/home/app  
  
COPY package.json bower.json .bowerrc $HOME/harpi/  
RUN chown -R app:app $HOME/*  
  
USER app  
WORKDIR $HOME/harpi  
RUN npm install  
  
USER root  
COPY . $HOME/harpi  
RUN chown -R app:app $HOME/*  
USER app  
  
# Port 3000 for server  
EXPOSE 3000  
CMD ["grunt", "prod", "--force"]  
  

