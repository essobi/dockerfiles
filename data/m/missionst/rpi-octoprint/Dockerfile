# Mission Street Manufacturing  
# OctoPrint on Raspberry Pi  
#  
# VERSION 0.0.2  
FROM missionst/rpi-pythonbase  
MAINTAINER Gabe Rosenhouse <gabe@missionst.com>  
  
RUN apt-get install -y python-flask python-werkzeug python-tornado python-
numpy python-netaddr && apt-get clean  
  
# OctoPrint requirements, but before the ADD line, so its cached  
RUN pip install flask==0.9 werkzeug==0.8.3 tornado==3.0.2 sockjs-
tornado>=1.0.0 PyYAML==3.10 Flask-Login==0.2.2 Flask-Principal==0.3.5
numpy>=1.6.2 pyserial>=2.6 netaddr>=0.7.10  
  
ADD OctoPrint /OctoPrint  
  
EXPOSE 5000  
  
# flag to run as root.  
CMD ["/OctoPrint/run", "--iknowwhatimdoing"]

