### Dockerfile  
#  
# See https://github.com/reconnix/docker  
FROM ubuntu:14.10  
MAINTAINER Russ McKendrick <russ.mckendrick@reconnix.com>  
  
RUN sudo useradd vagrant -u 666 && sudo mkhomedir_helper vagrant && sudo mkdir
/home/vagrant/data/ && sudo touch /home/vagrant/data/wibble && sudo chown -R
vagrant:vagrant /home/vagrant/data/ && sudo chmod -R 777 /home/vagrant/data/
&& sudo chmod -R 777 /root  
RUN sudo apt-get update -y && sudo apt-get install -y nodejs nodejs-legacy npm
git curl ruby ruby-dev  
RUN sudo gem install sass && sudo gem install compass  
RUN sudo npm install -g bower yo grunt-cli generator-webapp generator-backbone
generator-angular  
RUN sudo curl -L
https://gist.githubusercontent.com/russmckendrick/4de2658d97fa466644fb/raw/24003d97212f350498d6e56b1e3c22a299119134/MOTD.txt
> /home/vagrant/message && sudo chown vagrant:vagrant /home/vagrant/message

