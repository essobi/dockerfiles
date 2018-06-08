#  
# Python runtime Dockerfile  
#  
# https://github.com/dockerfile/python-runtime  
#  
# Pull base image.  
FROM gici/python:2  
# upgrade pip version to latest  
ONBUILD RUN pip install --upgrade pip  
  
# Set instructions on build.  
ONBUILD ADD apt-requirements.txt /app/  
ONBUILD RUN apt-get update && \  
apt-get -y install $(grep -vE "^\s*#" /app/apt-requirements.txt | tr "\n" " ")
&& \  
rm -rf /var/lib/apt/lists/*  
ONBUILD ADD requirements.txt /app/  
  
# allow passing pip index to private repo as build arg  
ONBUILD ARG PIP_INDEX_URL=https://pypi.python.org/simple  
  
# using 'process-dependency-links' for private repo's  
# it's deprecated but won't be removed until pip supports  
# direct-links, which won't happen soon :)  
# further read: https://github.com/pypa/pip/issues/2023#issuecomment-76086349  
ONBUILD RUN pip install -i $PIP_INDEX_URL \--no-cache-dir --process-
dependency-links -r /app/requirements.txt  
ONBUILD ADD . /app  
  
# Define working directory.  
WORKDIR /app  
  
# Define default command.  
CMD ["/usr/bin/python", "main.py"]  

