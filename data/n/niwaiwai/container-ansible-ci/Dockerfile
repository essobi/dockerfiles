FROM ubuntu  
  
# apt-getをアップデート  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# wgetをインストール  
RUN apt-get install -y wget  
  
# build-essentialをインストール  
RUN apt-get install -y build-essential  
  
# Ansibleをインストール  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:ansible/ansible  
RUN apt-get update  
RUN apt-get install -y ansible  
  
# Vagrantをインストール  
RUN wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.4_x86_64.deb  
RUN dpkg -i vagrant_1.7.4_x86_64.deb  
  
# Vagrantプラグインをインストール  
RUN vagrant plugin install vagrant-digitalocean  
  
# NPMをインストール  
RUN apt-get install -y nodejs npm  
  
# NPMのグローバルモジュールをインストール  
RUN npm install -g gulp  

