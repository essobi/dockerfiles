FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y build-essential libssl-dev git curl  
  
RUN git clone https://github.com/creationix/nvm.git  
  
ENV NODE_VERSION v0.11.14  
RUN echo 'source /nvm/nvm.sh && nvm install ${NODE_VERSION}' | bash -l  
ENV PATH /nvm/${NODE_VERSION}/bin:${PATH}  
  
RUN npm i gulp -g  
RUN npm i bower -g  
  
RUN \  
apt-get install -y ruby ruby-dev ruby-bundler && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install compass  

