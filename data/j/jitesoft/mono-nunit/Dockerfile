FROM mono:latest  
MAINTAINER Johannes Tegnér <johannes@jitesoft.com>  
  
ENV TEST_PROJECTS="" SOLUTIONS=""  
RUN mkdir -p /app /nunit  
VOLUME /app  
COPY ./run.sh /usr/src/app/run.sh  
CMD ["/bin/bash", "-C", "/usr/src/app/run.sh"]  

