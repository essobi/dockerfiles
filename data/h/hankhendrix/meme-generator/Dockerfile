FROM ubuntu:14.04  
MAINTAINER Chris Saunders <slapheadted@gmail.com>  
  
RUN apt-get install --yes wget  
  
# INSTALL GIT  
RUN apt-get install --yes git  
  
# INSTALL NODE - http://askubuntu.com/questions/672994/how-to-install-
nodejs-4-on-ubuntu-15-04-64-bit-edition  
RUN wget -qO- https://deb.nodesource.com/setup_4.x | sudo bash  
RUN apt-get install --yes nodejs  
  
# INSTALL BOWER  
RUN sudo npm install -g bower@1.7.7  
  
# INSTALL GULP  
RUN npm install -g gulp@3.9.1  
  
# COPY POLYMER  
COPY . /src  
  
WORKDIR /src  
  
RUN npm install  
  
RUN bower --allow-root install --force-latest  
  
EXPOSE 5000  
CMD gulp serve  

