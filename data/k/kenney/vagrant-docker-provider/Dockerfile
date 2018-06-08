# ubuntu 15.10  
FROM kenneyhe/ubuntu-slim:0.1  
RUN apt-get update && apt-get install wget bash -y  
RUN wget -qO /tmp/vagrant.deb
https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1_x86_64.deb  
RUN dpkg -i /tmp/vagrant.deb && rm -f /tmp/vagrant.deb  
RUN wget -qO- http://get.docker.com/ | sh  
RUN apt-get autoremove  
RUN usermod -aG docker root  
RUN vagrant plugin install docker  

