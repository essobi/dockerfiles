FROM ubuntu:16.04  
ADD install.sh /tmp/install.sh  
RUN sh /tmp/install.sh  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV PYTHONUNBUFFERED 1  
ENV PIP_NO_CACHE_DIR off  
  
RUN curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-
pipenv.py | python  
  
RUN mkdir -p /opt/pipenv/  
ADD Pipfile Pipfile.lock /opt/pipenv/  
WORKDIR /opt/pipenv/  
RUN pipenv install --deploy --system  

