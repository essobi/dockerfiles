FROM python:3.6.1  
RUN apt-get update \  
&& apt-get install -y gettext graphviz \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip install -U setuptools pip  
RUN mkdir -p /doc  
WORKDIR /doc  
COPY ./requirements.txt /doc/requirements.txt  
RUN pip install -r /doc/requirements.txt  
RUN pip install https://github.com/shimizukawa/sphinxcontrib-
feed/archive/master.zip  
  
CMD bash  

