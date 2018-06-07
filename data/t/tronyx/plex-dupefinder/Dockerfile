FROM python:3.5-alpine  
MAINTAINER christronyxyocum  
  
# Install Python modules  
RUN \  
pip install --disable-pip-version-check --no-cache-dir -U \  
requests \  
plexapi==3.0.6 \  
attrdict==2.0.0  
  
# Add local files  
COPY root/ /  
COPY config.py /app  
COPY plexdupes.py /app  

