FROM tcloud/ubuntu-jdk:8  
MAINTAINER tcloud  
  
# RUN bash -c "$(curl -s
https://raw.githubusercontent.com/actionml/PredictionIO/master/bin/install.sh)"  
ADD install.sh /opt/install.sh  
  
RUN chmod +x /opt/install.sh && \  
bash /opt/install.sh -y  
  
VOLUME ["/data","/log"]  
  
WORKDIR /data  
  
CMD ["/sbin/my_init"]  
  
# Clean up  
RUN sudo apt-get clean && \  
sudo apt-get autoremove -y && \  
sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

