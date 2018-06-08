FROM nicolargo/glances  
MAINTAINER <https://github.com/FuntwoX>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
COPY config/glances.conf /glances/conf/glances.conf  
CMD python -m glances -C /glances/conf/glances.conf $GLANCES_OPT

