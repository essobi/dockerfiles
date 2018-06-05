FROM python:2-slim  
  
MAINTAINER Gary Reynolds <gary@touch.asn.au>  
  
RUN apt-get update && apt-get -y install libmagic1 libzbar0 && apt-get clean  
  
RUN pip install --no-cache-dir gunicorn pillow python-magic  
  
COPY zbar-0.10-cp27-cp27mu-linux_x86_64.whl /tmp  
RUN pip install --no-cache-dir /tmp/zbar-0.10-cp27-cp27mu-linux_x86_64.whl  
  
COPY wsgi.py /  
  
EXPOSE 8000  
CMD ["gunicorn", "wsgi", "-b", "0.0.0.0:8000"]  

