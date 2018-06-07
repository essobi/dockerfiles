FROM ubuntu:14.04  
RUN apt-get update -y && apt-get -y install sudo  
RUN sudo apt-get install openjdk-7-jdk -y  
RUN sudo apt-get install git -y  
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker
sudo  
RUN sudo apt-get install mysql-server-5.5 -y && sudo mysql_install_db  
RUN sudo service mysql start && /usr/bin/mysqladmin -u root password 'secret'  
RUN sudo apt-get install maven -y  
# COPY settings.xml /root/.m2/  
RUN mvn --version && sudo service mysql start && service mysql status  
RUN sudo service mysql start && echo "CREATE DATABASE skeleton /*\\!40100
DEFAULT CHARACTER SET utf8 */;" | mysql -uroot -psecret  
RUN sudo apt-get install nodejs -y  
RUN sudo apt-get install npm -y  
RUN sudo npm install bower -g -y && sudo ln -s /usr/bin/nodejs /usr/bin/node  
  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
  
ENTRYPOINT service mysql start && /bin/bash  
  
EXPOSE 3306

