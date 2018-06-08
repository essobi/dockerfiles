FROM ubuntu:14.04  
RUN apt-get update  
  
RUN apt-get update \  
&& apt-get install -yf python \  
&& apt-get install -yf python-pip \  
&& apt-get install -yf python-dev \  
&& pip install --upgrade pip \  
&& pip install virtualenv \  
&& pip install invoke  
  
ADD tasks.py /tmp/tasks.py  
WORKDIR /tmp  
# CMD [ 'inv' , 'install' ]  
# CMD [ "python", "./tasks.py" ]  
RUN inv install  
  
CMD ["/bin/bash"]  

