FROM continuumio/anaconda3:4.3.1  
MAINTAINER Anand Chitipothu <anand@rorodata.com>  
  
RUN /opt/conda/bin/conda install jupyter -y --quiet  
RUN pip install tensorflow keras virtualenv  
  
ENV PYTHONUNBUFFERED=x  
ENV HOME=/data  
WORKDIR /data  
  
CMD ["/bin/bash"]  

