FROM ruby:2.3-onbuild  
  
RUN apt-get update && \  
apt-get install -y \  
openjpeg-tools \  
python-pip \  
python-dev \  
python-gdal \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install -r python_requirements.txt  

