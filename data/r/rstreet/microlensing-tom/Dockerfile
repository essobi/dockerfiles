FROM centos:7  
EXPOSE 80  
ENTRYPOINT [ "/init" ]  
  
# Establish user ID of container while running  
RUN groupadd -g 20000 domainusers \  
&& useradd -u 20007 -g 20000 -c "Microlensing user" -d /home/robouser -s
/bin/bash robouser  
  
# install packages  
RUN yum -y install epel-release \  
&& yum -y install nginx python-pip supervisor python-devel uwsgi-plugin-python
\  
&& yum -y install gcc g++ gcc-gfortran \  
&& yum -y update \  
&& yum -y clean all  
  
# system configuration  
COPY docker/ /  
  
# install python requirements  
COPY pip-requirements.txt /var/www/spitzermicrolensing/  
RUN pip install --upgrade pip \  
&& pip install numpy \  
&& pip install -r /var/www/spitzermicrolensing/pip-requirements.txt \  
&& rm -rf ~/.cache ~/.pip  
  
# copy application  
COPY . /var/www/spitzermicrolensing/  

