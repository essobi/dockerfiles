# Base Image  
FROM python:2.7.12  
# Metadata  
LABEL base.image="python:2.7.12"  
LABEL version="2.7.12"  
LABEL software="Python"  
LABEL software.version="2.7.12"  
LABEL description="Andrew's python set-up"  
LABEL documentation="  
  
# Maintainer  
MAINTAINER Andrew Wong <nderoo.wong@gmail.com>  
  
# Python Package Install  
RUN pip install illuminate && \  
pip install beautifulsoup4 && \  
pip install lxml && \  
pip install Jinja2 && \  
pip install weasyprint  

