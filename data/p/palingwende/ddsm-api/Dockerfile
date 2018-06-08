FROM ubuntu:14.04  
# Update packages  
RUN apt-get update -y  
  
# Install Python Setuptools  
RUN apt-get install -y python-setuptools  
  
# Install git  
RUN apt-get install -y git  
  
# Install ddsm-db  
RUN rm -rf ddsm-db  
RUN git clone https://github.com/faical-yannick-congo/ddsm-db.git  
RUN cd /ddsm-db; python setup.py develop  
  
# Install pip  
RUN easy_install pip  
  
# Add and install Python modules  
ADD requirements.txt /src/requirements.txt  
RUN cd ..  
RUN cd /src; pip install -r requirements.txt  
RUN cd ..  
  
# Bundle app source  
ADD . /src  
  
# Expose  
EXPOSE 5100  
# Run  
CMD ["python", "/src/run.py", "--host=0.0.0.0", "--port=5100"]

