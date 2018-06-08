FROM ubuntu  
  
# apt-getをアップデート  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install wget make g++ libssl-dev git  
  
# NPMをインストール  
RUN apt-get -y install nodejs npm  
  
# NPMのグローバルモジュールをインストール  
RUN npm install -g gulp  
  
# Gemをインストール  
RUN apt-get install -y ruby ruby-dev  
  
# Gemのグローバルモジュールをインストール  
RUN gem install bundler  
RUN gem install compass  
  
# Fabricインストール  
RUN apt-get -y install fabric  

