FROM sunside/storm:latest  
MAINTAINER Markus Mayer <widemeadows@gmail.com>  
  
EXPOSE 6700 6701 6702 6703 8000  
RUN /usr/bin/config-supervisord.sh supervisor  
RUN /usr/bin/config-supervisord.sh logviewer  
CMD /usr/bin/start-supervisord.sh  

