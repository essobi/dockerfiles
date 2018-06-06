FROM python:3.6-alpine  
  
ENV INSTALL_LOCATION=/http-status-puppet  
  
WORKDIR "${INSTALL_LOCATION}"  
ADD requirements.txt requirements.txt  
RUN pip install --disable-pip-version-check -r requirements.txt  
  
ADD . ./  
RUN python setup.py install  
  
CMD ["python", "httpstatuspuppet/entrypoint.py"]  

