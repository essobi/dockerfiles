FROM nacyot/ubuntu  
MAINTAINER Manhui Han <hanmanhui@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get -y install python python-dev python-pip  
RUN pip install 'Twisted<12.0'  
  
WORKDIR /usr/local/src  
  
RUN git clone https://github.com/graphite-project/carbon.git  
RUN git clone https://github.com/graphite-project/whisper.git  
RUN cd whisper && git checkout master && python setup.py install  
RUN cd carbon && git checkout 0.9.12 && python setup.py install  

