FROM centos  
MAINTAINER Michael Davis "michael@damaru.com"  
ENV REFRESHED_AT 2016-03-20  
RUN yum -y install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y install ImageMagick  
RUN yum -y install ffmpeg  
RUN yum -y install python-pip  
RUN pip install boto  
RUN pip install requests  
RUN pip install web.py  
# just for testing...  
ADD server.py .  
ADD video.py .  
ADD client.py .  
EXPOSE 80  
CMD ["python", "server.py", "80"]  
  

