FROM eclipse/ubuntu_jdk8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sudo apt-get update && sudo apt-get install -y \  
nano && \  
sudo -E bash -c "apt-get -y --no-install-recommends install mysql-server" && \  
sudo apt-get clean && \  
sudo apt-get -y autoremove && \  
sudo apt-get -y clean && \  
sudo rm -rf /var/lib/apt/lists/* && \  
sudo sed -i.bak 's/127.0.0.1/0.0.0.0/g' /etc/mysql/my.cnf && \  
sudo service mysql restart #&& \  
#sudo mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'; FLUSH
PRIVILEGES;" && \  
#sudo service mysql restart  
  
WORKDIR /projects  
  
CMD tail -f /dev/null  

