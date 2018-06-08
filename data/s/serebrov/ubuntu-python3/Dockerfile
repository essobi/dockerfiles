FROM ubuntu:xenial  
RUN apt-get update  
RUN apt-get install -y locales python3-pip python3-dev python3-virtualenv
fabric \  
libpq-dev libjpeg-dev libxml2-dev libxslt-dev libfreetype6-dev libffi-dev \  
postgresql-client git curl wget  
# Without LC_ALL setting httpretty installation fails  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Needed for pytest when run tests with docker exec -it  
ENV TERM xterm  
  
# Install python dev tools  
RUN pip3 install pytest \  
pytest-cov \  
pytest-greendots \  
pytest-flask \  
coverage \  
pylint \  
pylint-flask \  
flake8 \  
mypy  

