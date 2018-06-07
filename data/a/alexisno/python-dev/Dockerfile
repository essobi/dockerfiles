# Pull base image  
FROM alexisno/ubuntu-dev  
  
# Install Python  
RUN apt-get update &&\  
apt-get install -y python python-dev python-pip python3-pip python-virtualenv
&&\  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install useful modules for development environment  
RUN pip install pudb ipython &&\  
python3 -m pip install pudb ipython  
  
USER dev  
  
CMD ["python"]  

