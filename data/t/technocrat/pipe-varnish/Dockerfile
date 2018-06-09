FROM ubuntu:14.04  
  
RUN sudo apt-get -y update && \  
sudo apt-get -y install apt-transport-https && \  
sudo apt-get -y install curl && \  
sudo curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \  
sudo echo "deb https://repo.varnish-cache.org/ubuntu/ precise varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
sudo apt-get -y install varnish  
  
ADD default.vcl /etc/varnish/default.vcl  
  
CMD varnishd -a :80 \  
-T localhost:6082 \  
-f /etc/varnish/default.vcl \  
-S /etc/varnish/secret \  
-s malloc,1024m \  
-F  
  
EXPOSE 80  
EXPOSE 6082  

