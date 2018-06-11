FROM wadoon/flaskapp  
  
MAINTAINER Alexander Weigl <Alexander.Weigl@student.kit.edu>  
  
WORKDIR /app  
  
EXPOSE 5000  
RUN apt-get update  
RUN apt-get install -y libxml2-dev libxslt1-dev python-dev libz-dev python-
vtk6 git wget  
  
RUN wget
'https://github.com/CognitionGuidedSurgery/elasticity/blob/master/bin/elasticity.lx64?raw=true'
-O /bin/elasticity  
  
ADD . /app  
ADD ./gunicornconfig.py /etc/gunicornconfig.py  
  
RUN pip install -r /app/requirements.txt  
  
ENV PYTHONPATH /app  
  
ENTRYPOINT gunicorn -c /etc/gunicornconfig.py restflow.server:app  

