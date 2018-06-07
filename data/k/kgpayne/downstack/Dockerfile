FROM ubuntu:trusty  
MAINTAINER kp <kpsupernut@gmail.com>  
  
#Install Python 7z and Boto  
RUN apt-get -q update && apt-get install -qy python-pip \  
python-dev \  
build-essential \  
p7zip \  
p7zip-full \  
&& pip install boto  
  
VOLUME ["/scripts"]  
VOLUME ["/destination"]  
  
# Call python script  
CMD ["python", "/scripts/04downloadfroms3.py"]  

