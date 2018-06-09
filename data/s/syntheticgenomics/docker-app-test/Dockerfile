FROM python:2.7.14  
  
RUN apt-get update && apt-get install -y \  
libldap2-dev \  
libsasl2-dev \  
python-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install appdynamics  
  
RUN pip install uWSGI~=2.0 tox  

