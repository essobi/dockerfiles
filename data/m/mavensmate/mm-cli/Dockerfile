FROM ubuntu:trusty  
MAINTAINER mavensmate <info@mavensmate.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python python-dev
python-pip libyaml-dev  
ADD . /mm  
RUN pip install jinja2 suds keyring markupsafe pyyaml requests mock  
  
ENTRYPOINT ["python mm.py"]  
  
CMD ["--help"]

