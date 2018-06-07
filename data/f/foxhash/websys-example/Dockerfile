# Base image: ubuntu 16.04  
FROM ubuntu:16.04  
# Install python and git  
RUN apt-get update  
RUN apt-get install -y \  
python \  
python-pip \  
git  
RUN apt-get clean  
  
# Update pip  
RUN pip install --upgrade pip  
  
# Add central pip requirements file  
ADD requirements.txt /root/.  
  
# Install requirements  
RUN pip install -r /root/requirements.txt  
  
# Copy Python API  
COPY python_api /root/python_api  
  
CMD ["python", "/root/python_api/app.py"]  

