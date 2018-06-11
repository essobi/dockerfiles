FROM tensorflow/tensorflow:0.12.1  
RUN apt-get -y update  
RUN apt-get -y install python-opencv  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define default command.  
CMD ["bash"]  

