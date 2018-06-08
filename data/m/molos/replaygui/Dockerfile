FROM ubuntu:14.04  
RUN apt-get update && apt-get -y install python2.7  
RUN apt-get install -y python-pip  
  
RUN pip install Flask  
RUN pip install ibmiotf  
RUN pip install requests  
RUN pip install flask-socketio --upgrade  
RUN pip install python-socketio --upgrade  
RUN pip install python-engineio --upgrade  
RUN pip install cloudant  
  
ENV PORT=5000  
EXPOSE 5000  
ADD ./SIARA /opt/SIARA/  
WORKDIR /opt/SIARA/  
  
CMD sleep 80 && python testGUI.py  

