FROM jujusolutions/charmbox  
  
VOLUME ["/home/ubuntu/.juju", "/home/ubuntu/mojo"]  
  
RUN add-apt-repository -y ppa:mojo-maintainers/ppa && apt-get update -qqy &&
apt-get install -qy mojo python-swiftclient python-glanceclient python-
heatclient python-novaclient python-pika amulet && usermod -a -G mojo ubuntu  
  
ADD cleanup.sh /cleanup.sh  
RUN /cleanup.sh  
  
ADD go-mojo /usr/local/bin/go-mojo  
ADD setup_mojo.sh /home/ubuntu/setup_mojo.sh

