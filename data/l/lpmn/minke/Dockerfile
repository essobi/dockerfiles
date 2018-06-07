FROM lpmn/lalsuite:minke-latest  
MAINTAINER Daniel Williams <daniel.wiliams@ligo.org>  
  
RUN git config --global user.name "Anonymous" \  
&& git config --global user.email anonymous@example.com  
  
RUN git clone https://github.com/transientlunatic/minke.git \  
&& cd minke \  
&& python setup.py install  

