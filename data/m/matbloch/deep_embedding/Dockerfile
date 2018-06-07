# base image: kaixhin/caffe  
FROM kaixhin/caffe  
  
# File Author / Maintainer  
MAINTAINER Matthias Bloch  
  
############################################################  
# Dockerfile to build Identification Node Container  
############################################################  
  
# sudo add-apt-repository python-opencv  
  
# Copy the application folder inside the container  
ADD . /uids  
  
ENV PYTHONPATH $PYTHONPATH:/uids  
  
# install requirements  
RUN cd /uids && \  
pip2 install -r requirements.txt  
  
# inform about port listening (use -p when you start the container)  
EXPOSE 8080  
  
# Set the default directory where CMD will execute  
WORKDIR /uids  

