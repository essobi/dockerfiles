FROM ubuntu:14.04  
RUN apt-get update -y  
RUN apt-get -y install build-essential curl chrpath libssl-dev libxft-dev
python  
  
# install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# install yarn  
RUN npm install -g yarn  
  
# install phantomjs-prebuilt  
RUN yarn global add backstopjs@2.2.0 http-server  
  
# add run.sh  
COPY ./run.sh /  
  
WORKDIR /app  
  
ENTRYPOINT ["/run.sh"]  
  
# use reference as default commande eg. backstop reference  
CMD ["reference"]  

