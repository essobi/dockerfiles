FROM slaff/docker-php  
RUN echo 'Start building HippyVM'  
MAINTAINER Slavey Karadzhov <slavey@zend.com>  
WORKDIR /home/dev/hippyvm  
RUN git pull  
RUN apt-get install -y libffi-dev  
# RUN python /home/dev/pypy/rpython/bin/rpython -Ojit targethippy.py  

