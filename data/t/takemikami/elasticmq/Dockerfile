FROM base/archlinux  
  
RUN pacman -Syy && pacman -S --noconfirm wget jdk8-openjdk  
  
RUN mkdir /opt/elasticmq \  
&& cd /opt/elasticmq \  
&& wget https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-0.8.8.jar  
  
ADD elasticmq /usr/local/bin/  
RUN chmod +x /usr/local/bin/elasticmq  
  
CMD ["/usr/local/bin/elasticmq"]  

