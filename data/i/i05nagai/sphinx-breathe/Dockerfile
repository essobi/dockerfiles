FROM python:3.6.2-slim  
MAINTAINER i05nagai  
  
ADD sphinxrenderer.py.patch /tmp  
RUN apt-get update \  
&& apt-get install -y \  
graphviz \  
doxygen \  
patch \  
&& pip install \  
sphinx==1.6.3 \  
breathe==4.6.0 \  
sphinx_rtd_theme \  
&& cd /usr/local/lib/python3.6/site-packages/breathe/renderer \  
&& patch < /tmp/sphinxrenderer.py.patch  
  

