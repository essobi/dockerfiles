FROM centos:7  
RUN mkdir /opt/railnation && \  
/usr/bin/curl 'https://bootstrap.pypa.io/get-pip.py' | /usr/bin/python && \  
pip install cherrypy requests jsonschema  
  
ENV PYTHONPATH /opt/railnation/lib  
  
EXPOSE 8080  
ENTRYPOINT ["/bin/sh", "/opt/railnation/start.sh"]  
CMD []  
  
ADD . /opt/railnation  
  

