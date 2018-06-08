FROM python:3.6  
RUN apt-get update  
RUN apt-get install -yq build-essential git libstdc++6 liblapack-dev gcc musl-
dev  
RUN apt-get install -yq postgresql postgresql-contrib libpq-dev  
  
# Install Dockerize: it's useful (e.g. when telling a container to wait for
its postgres  
# database to start up)  
# https://github.com/jwilder/dockerize#ubuntu-images  
RUN apt-get install -yq wget  
ENV DOCKERIZE_VERSION v0.6.1  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# It's always good practice to use a virtualenv, so we create one beforehand.  
RUN mkdir -p /root  
RUN python3 -m venv /root/virtualenv  
  
RUN /root/virtualenv/bin/pip install 'wheel ~= 0.30'  
  
# Some standard utilities we need for checking code.  
RUN /root/virtualenv/bin/pip install 'pylint ~= 1.7'  
RUN /root/virtualenv/bin/pip install 'pytest ~= 3.1'  
RUN /root/virtualenv/bin/pip install 'pytest-cov ~= 2.5'  
  
ADD pylintrc /root/pylintrc  
ADD run_tests /root/run_tests  
  

