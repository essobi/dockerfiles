# Python-CI  
#  
# VERSION 0.0.1  
FROM python:3.6.3  
LABEL Description="A simple container with Python3 and packages which make CI
easier in environments such as Jenkins." Vendor="Octoberist" Version="1.0"  
LABEL maintainer="Derek Sudduth <derek.sudduth@gmail.com>"  
  
# Add Jenkins User  
RUN useradd -r -u 10000 -d /home/jenkins -U jenkins  
  
# Install Pipenv  
RUN set -ex && pip install --no-cache-dir pipenv  
  
# Install other Python packages for CI environment  
RUN pip install --no-cache-dir \  
flake8 \  
pytest \  
pytest-cov \  
mock \  
pytest-mock \  
pytest-xdist \  
twine \  
tox \  
gitpython \  
invoke \  
jinja2 \  
pyinstaller \  
coverage  
  
USER jenkins  
WORKDIR /home/jenkins  
  
CMD ["/bin/sh"]  

