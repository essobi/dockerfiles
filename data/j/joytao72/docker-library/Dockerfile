FROM python:2.7  
ADD scripts/ /usr/local/cbpython/scripts/  
ADD libs/ /usr/local/cbpython/libs/  
ADD pyrfc/ /usr/local/cbpython/pyrfc/  
  
RUN cp -r /usr/local/cbpython/libs/* /usr/lib/  
  
RUN apt-get update  
RUN apt-get install -y python-setuptools  
  
RUN cd /usr/local/cbpython/pyrfc; easy_install
pyrfc-1.9.3-py2.7-linux-x86_64.egg  
  
#CMD ["python", "/usr/local/cbpython/scripts/pythonscript.py"]  
CMD ["python2"]

