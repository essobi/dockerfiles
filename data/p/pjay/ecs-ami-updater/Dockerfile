FROM python:3-slim  
  
MAINTAINER Philip Jay <phil@jay.id.au>  
  
RUN apt-get update \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD requirements.txt /tmp/reqs/  
  
RUN pip install \  
\--no-cache-dir \  
\--upgrade \  
\--requirement /tmp/reqs/requirements.txt  
  
ADD ecs_ami_updater.py /app/  
  
ENTRYPOINT ["python", "/app/ecs_ami_updater.py"]  

