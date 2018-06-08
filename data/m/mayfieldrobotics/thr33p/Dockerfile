FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
python \  
python-dev \  
python-pip  
  
ADD . /opt/thr33p/  
WORKDIR /opt/thr33p/  
RUN pip install -e .  
RUN pip install "gevent>=1,<2" "gunicorn>=19,<20" "setproctitle>=1.1.8,<2.0"  
  
ENTRYPOINT ["gunicorn", "thr33p:app", "--bind", "0.0.0.0:8000"]  

