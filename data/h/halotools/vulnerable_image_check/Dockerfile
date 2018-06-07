FROM halotools/python-sdk:ubuntu-16.04_sdk-1.0.4_2018-01-22  
MAINTAINER toolbox@cloudpassage.com  
  
RUN mkdir /vulnerable_image_check  
  
COPY runner.py /  
  
COPY vulnerable_image_check/ /vulnerable_image_check/  
  
WORKDIR /  
  
CMD ["/usr/bin/python", "runner.py"]  

