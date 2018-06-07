FROM ubuntu:xenial  
MAINTAINER Artem Sidorenko <artem@posteo.de>  
  
RUN apt-get update ;\  
apt-get -y install sudo ;\  
apt-get -y install openssh-server supervisor man-db rsync ;\  
apt-get -y install git curl wget ;\  
rm -rf /var/lib/apt/lists/* ;\  
mkdir /var/run/sshd  
  
#password is vagrant  
RUN useradd -m -p
'$6$UFLdXsV4$hnP4J2l8w02eCoj7ogsQZ0wdEImAKtzIoQqmrNLEXkyI1UsuPPofdpf4DMViq4QPdFVOz0yekQ35lgaFUB6SF/'
-s /bin/bash vagrant  
  
COPY assets /  
  
RUN chown -R vagrant:vagrant /home/vagrant ;\  
chmod 600 /home/vagrant/.ssh/authorized_keys  
  
CMD supervisord -c /etc/supervisord.conf  
EXPOSE 22  

