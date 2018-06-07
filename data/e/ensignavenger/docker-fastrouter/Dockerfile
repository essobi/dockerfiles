FROM ensignavenger/uwsgi-py3  
  
MAINTAINER James Lee Vann  
  
VOLUME ["/subscription"]  
  
ADD run.sh /run.sh  
RUN ["chmod", "+x", "run.sh"]  
  
EXPOSE 80 443  
CMD ["/run.sh"]  
  

