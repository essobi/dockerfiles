from openhab/openhab:2.0.0-amd64  
  
MAINTAINER Marco Nunez <setterlee@gmail.com>  
  
ENV TZ=Chile/Continental  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["gosu", "openhab", "./start.sh"]  

