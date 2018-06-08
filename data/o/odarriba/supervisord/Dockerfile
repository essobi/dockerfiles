FROM ubuntu:14.04  
  
MAINTAINER Óscar de Arriba <odarriba@gmail.com>  
  
#####################  
# Update the system #  
#####################  
RUN apt-get update && \  
apt-get dist-upgrade -y  
  
#######################  
# Install supervisord #  
#######################  
RUN apt-get install -y supervisor python-pip && \  
pip install supervisor-stdout && \  
mkdir -p /var/log/supervisor && \  
echo " \  
/etc/init.d/supervisor start" >> /etc/bash.bashrc  
  
ADD config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/bin/bash"]

