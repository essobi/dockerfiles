FROM python:2.7  
MAINTAINER uoks <uolgks@gmail.com>  
  
RUN git clone https://github.com/9miao/Firefly Firefly \  
&& cd ./Firefly \  
&& python ./setup.py install  
  
WORKDIR /root  
  
CMD ["/bin/bash"]  
  

