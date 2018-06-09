FROM jupyter/scipy-notebook  
  
MAINTAINER Tyler Erickson <tylere@google.com>  
  
USER root  
  
# Install Earth Engine non-Python dependencies  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
libffi-dev \  
git \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Earth Engine packages for Python 2  
RUN pip2 install cryptography  
RUN pip2 install earthengine-api  
  
# Install Earth Engine packages for Python 3  
RUN pip3 install cryptography  
RUN pip3 install earthengine-api  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER jovyan

