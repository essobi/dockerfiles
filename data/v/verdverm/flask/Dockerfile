FROM google/debian:wheezy  
MAINTAINER verdverm@gmail.com  
  
# Update stuff  
RUN apt-get update  
  
# Install Python Setuptools  
RUN apt-get --no-install-recommends install -y python-setuptools build-
essential python-dev libpq-dev ca-certificates  
  
# Install pip  
RUN easy_install pip  
  
ADD requirements.txt /tmp/requirements.txt  
  
# Install requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
EXPOSE 5000  
VOLUME ["/src"]  
WORKDIR /src  
  
ENTRYPOINT ["python", "/src/run.py"]  
CMD ["runserver"]  

