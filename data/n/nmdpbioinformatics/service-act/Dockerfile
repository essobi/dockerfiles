FROM ubuntu:17.10  
MAINTAINER Mike Halagan <mhalagan@nmdp.org>  
  
ADD . opt/  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q  
  
RUN apt-get install -qy wget curl build-essential cpp git \  
python3.6 python3-pip python3-dev \  
python3-setuptools uwsgi-plugin-python3 \  
python3.6-dev libxft-dev mysql-server \  
python-mysqldb python3-mysql.connector \  
python3-setuptools uwsgi-plugin-python3 \  
&& curl https://bootstrap.pypa.io/get-pip.py | python3.6 \  
&& pip3 install --upgrade pip  
  
RUN apt-get install clustalo -y  
RUN apt-get install ncbi-blast+ -y  
  
WORKDIR opt/  
  
RUN pip3 install -r requirements.txt  
  
EXPOSE 8080  
EXPOSE 5000  
CMD python3.6 app.py  

