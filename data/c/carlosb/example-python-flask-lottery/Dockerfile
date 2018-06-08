FROM ubuntu:14.04  
MAINTAINER Kate Heddleston <kate@makemeup.co>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && apt-get
install -y build-essential git python python-dev python-setuptools nginx
supervisor bcrypt libssl-dev libffi-dev libpq-dev vim redis-server rsyslog
wget  
RUN easy_install pip  
  
# Add github repo code to code file  
ADD . /code/  
WORKDIR code  
  
# Add requirements and install  
ADD ./files/requirements.txt /code/  
RUN pip install -r ./requirements.txt  
  
ENTRYPOINT ["python"]  
CMD ["run.py"]  
  

