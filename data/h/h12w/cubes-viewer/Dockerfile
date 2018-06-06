FROM django:python2  
MAINTAINER Hǎiliàng Wáng <w@h12.me>  
  
RUN apt-get update && \  
apt-get install --yes unzip \  
expect \  
&& \  
apt-get autoremove --yes  
  
RUN pip install django-piston \  
djangorestframework \  
requests  
  
ADD https://github.com/h12w/cubesviewer/archive/master.zip /tmp/cv.zip  
RUN unzip /tmp/cv.zip && \  
rm /tmp/cv.zip && \  
mv cubesviewer-master cubes-viewer  
  
WORKDIR cubes-viewer  
  
ENTRYPOINT ./run.sh  
  

