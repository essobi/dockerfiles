FROM dispel4py/storm:0.10.0  
MAINTAINER dispel4py  
  
EXPOSE 6700  
EXPOSE 6701  
EXPOSE 6702  
EXPOSE 6703  
EXPOSE 8000  
USER root  
RUN apt-get update  
RUN yes | apt-get install python-pip python-dev python-setuptools python-numpy
python-numpy-dev python-scipy python-matplotlib python-lxml python-sqlalchemy
python-suds  
RUN pip install networkx  
RUN pip install numpy  
RUN pip install obspy  
  
RUN /usr/bin/config-supervisord.sh supervisor  
RUN /usr/bin/config-supervisord.sh logviewer  
CMD /usr/bin/start-supervisor.sh  
  

