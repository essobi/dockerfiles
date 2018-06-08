#  
FROM edmooney/ubuntubase  
MAINTAINER edmooney@outlook.com  
# Add deps  
RUN apt-get update && apt-get install -y -qq git gunicorn wget libxml2
libxml2-dev libxslt1-dev python-libxslt1 build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip
lib32z1-dev  
RUN pip install flask  
RUN pip install readability-lxml  
WORKDIR /root  
RUN git clone https://bitbucket.org/edmooney/flask-readability.git  
  
EXPOSE 5000  
WORKDIR /root/flask-readability  
  
#RUN python app.py  

