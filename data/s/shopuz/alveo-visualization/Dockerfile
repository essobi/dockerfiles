FROM ubuntu:14.04  
RUN sudo apt-get install -y python  
RUN sudo apt-get update  
RUN sudo apt-get install -y git  
RUN sudo apt-get install -y python-setuptools  
  
RUN git clone https://github.com/shopuz/alveo_visualization.git  
  
RUN git clone https://github.com/Alveo/pyhcsvlab.git  
  
WORKDIR /pyhcsvlab  
RUN python setup.py install  
  
WORKDIR /alveo_visualization  
EXPOSE 8080  
CMD ["python", "temp.py"]

