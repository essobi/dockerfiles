FROM phusion/baseimage  
MAINTAINER Lu Han <lhan@xetus.com>  
  
#  
# Install need dependencies  
#  
RUN apt-get update &&\  
apt-get install -y python-setuptools &&\  
easy_install pip  
ADD requirements.txt /opt/aws-autosnap/requirements.txt  
RUN cd /opt/aws-autosnap; pip install -r requirements.txt  
  
# Bundle app source  
ADD config.sample /opt/aws-autosnap/config.py  
ADD autosnap.py /opt/aws-autosnap/autosnap.py  
ADD init.py /opt/aws-autosnap/init.py  
  
# Run the command on container startup  
CMD ["python", "/opt/aws-autosnap/init.py"]

