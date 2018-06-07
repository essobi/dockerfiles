# base image  
FROM python:3-alpine  
  
# requirements  
RUN set -ex \  
&& pip install --no-cache-dir \  
boto3==1.5.22  
  
# ecs deployer script  
ENV PYTHONUNBUFFERED 1  
COPY ecs_deployer.py /usr/local/bin/ecs_deployer.py  
  
# entrypoint / cmd  
ENTRYPOINT ["ecs_deployer.py"]  
CMD ["--help"]  

