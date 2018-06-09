FROM base/archlinux  
  
RUN pacman -Syy && pacman -S --noconfirm wget jdk8-openjdk  
  
RUN cd /tmp \  
&& wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz \  
&& mkdir /opt/dynamodblocal \  
&& cd /opt/dynamodblocal \  
&& tar zxf /tmp/dynamodb_local_latest.tar.gz \  
&& rm /tmp/* \  
&& mkdir /var/dynamodblocal  
  
ADD dynamodblocal /usr/local/bin/  
RUN chmod +x /usr/local/bin/dynamodblocal  
  
CMD ["/usr/local/bin/dynamodblocal"]  

