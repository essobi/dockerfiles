FROM wadoon/flaskapp  
  
MAINTAINER Alexander Weigl <alexander.weigl@student.kit.edu>  
  
  
  
EXPOSE 5000  
  
ADD dockerproviderconfig.py /etc/providerconfig.py  
ADD gunicornconfig.py /etc/gunicornconfig.py  
ADD . /app/  
  
WORKDIR /home  
  
ENV STORAGE_PROVIDER_CONFIG /etc/providerconfig.py  
ENV PYTHONPATH /app  
  
#ENTRYPOINT ['gunicorn' , '-c', '/etc/gunicornconfig.py']  
#ENTRYPOINT "/bin/bash" #DEBUGGING  
ENTRYPOINT gunicorn -c /etc/gunicornconfig.py storage.provider:app  

