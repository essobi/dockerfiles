FROM continuumio/anaconda  
  
MAINTAINER Hudl DS <keenan.hawekotte@hudl.com>  
  
RUN apt-get -y update && apt-get install -y g++  
RUN pip install keras  
  
EXPOSE 8888  
CMD ipython notebook --no-browser --port 8888 --ip=*

