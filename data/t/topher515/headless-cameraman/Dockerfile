FROM rosenhouse/phantomjs2:2.0.0  
MAINTAINER wilcox@zoomforth.com  
  
WORKDIR /opt  
  
EXPOSE 80  
RUN apt-get update  
RUN apt-get install -y python2.7 python-pip python-all-dev  
RUN pip install Flask==0.10.1 watchdog==0.8.2 CherryPy==3.8.0 redis==2.10.3  
  
ADD render.js /opt/render.js  
ADD serve.py /opt/serve.py  
  
CMD /usr/bin/python /opt/serve.py

