FROM linarotechnologies/minideb:stretch  
  
RUN install_packages python-pip libusb-1.0-0-dev libudev-dev  
  
RUN pip install setuptools wheel --upgrade && \  
pip install --pre -U pyocd  
  
CMD pyocd-flashtool  

