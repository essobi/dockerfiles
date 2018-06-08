FROM phusion/baseimage  
  
RUN apt-get update  
RUN apt-get install -y python3-dev python3-pip gcc libxml2-dev libxslt1-dev
zlib1g-dev  
  
RUN pip3 install --upgrade pip  
RUN pip3 install lxml flask flask_wtf urllib3 bs4 cherrypy  
  
COPY *.py /leocards/  
COPY static/* /leocards/static/  
COPY templates/* /leocards/templates/  
  
EXPOSE 5000  
WORKDIR /leocards  
ENTRYPOINT ["python3", "-u", "main.py"]

