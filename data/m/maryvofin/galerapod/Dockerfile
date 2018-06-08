FROM ubuntu:16.04  
#Adding repos and updating  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y apt-utils debconf-utils software-properties-common apt-
transport-https  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8  
RUN add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.1/ubuntu xenial main'  
RUN apt-get update  
RUN apt-get upgrade -y  
  
#Configurate debconf  
COPY debconfselections.conf /root/debconfselections.conf  
RUN debconf-set-selections /root/debconfselections.conf  
RUN rm /root/debconfselections.conf  
  
#Installing needed packages  
RUN apt-get -y install mariadb-server rsync  
#RUN systemctl stop mysql  
#Configuring cluster  
COPY galera.cnf /etc/mysql/conf.d/galera.cnf  
#RUN ufw allow 3306,4567,4568,4444/tcp  
#RUN ufw allow 4567/udp  
#TODO in kubernetes pod: this_node_ip, this_node_name

