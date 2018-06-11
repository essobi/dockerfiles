FROM ekazakov/python-opencv:py2.7  
RUN apt-get -y update  
RUN apt-get -y install python2.7-dev libboost-python-dev  
  
RUN pip install dlib==19.1.0  
RUN rm -rf /root/.cache  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
# Define default command.  
CMD ["bash"]  

