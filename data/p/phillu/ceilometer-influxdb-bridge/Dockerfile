FROM python:3  
MAINTAINER Phil Stelzer <phil@philstelzer.com>  
  
ENV OS_USERNAME demo  
ENV OS_PASSWORD openstack  
ENV OS_TENANT_NAME demo  
ENV OS_AUTH_URL "http://10.0.0.20:5000/v2.0"  
ENV STACK_ID 12345  
ENV FLASK_APP main.py  
  
ADD requirements.txt .  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
  
ADD envdefault.py .  
ADD main.py .  
  
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]  

