FROM python:2.7  
MAINTAINER Rogier Slag <rogier@magnet.me>  
  
RUN groupadd -r python && useradd -r -g python pythonuser  
RUN mkdir /zktop && chown pythonuser /zktop  
  
USER pythonuser  
RUN cd /zktop && git clone https://github.com/phunt/zktop.git .  
ADD entry.sh /zktop  
  
WORKDIR /zktop  
CMD ["/bin/bash", "/zktop/entry.sh"]  
  

