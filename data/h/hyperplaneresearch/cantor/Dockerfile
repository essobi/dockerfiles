FROM python:2  
  
RUN curl \--silent \--show-error \--retry 5 https://bootstrap.pypa.io/get-
pip.py | python2.7  
  
RUN pip install nose  
  
COPY ssh_config /root/.ssh/config  
COPY cantor_client /usr/bin/cantor_client

