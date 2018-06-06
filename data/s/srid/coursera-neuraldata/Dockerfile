FROM ubuntu:14.04  
RUN apt-get -y update  
RUN apt-get -y install python-numpy python-scipy python-matplotlib  
RUN apt-get -y install ipython ipython-notebook  
  
ADD . /app  
WORKDIR /app/my-work  
  
# For IPython notebook web port  
EXPOSE 8888  

