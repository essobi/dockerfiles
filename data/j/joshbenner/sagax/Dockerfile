FROM python:3.6-alpine3.7  
  
RUN apk add \--no-cache -t build-deps gcc musl-dev && \  
pip install \--no-cache-dir cython gunicorn && \  
pip install \--no-cache-dir \--no-binary falcon sagax[ldap] six==1.10.0 && \  
apk del build-deps  
  
CMD ["gunicorn", "--access-logfile", "/dev/stdout", "-w", "4",
"sagax.api:__hug_wsgi__"]  

