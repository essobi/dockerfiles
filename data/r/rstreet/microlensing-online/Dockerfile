FROM centos:7  
EXPOSE 80  
ENTRYPOINT [ "/init" ]  
  
# install packages  
RUN yum -y install epel-release \  
&& yum -y install nginx python-pip supervisor uwsgi-plugin-python \  
&& yum -y update \  
&& yum -y clean all  
  
# system configuration  
COPY docker/ /  
  
# install python requirements  
COPY pip-requirements.txt /var/www/microlensingonline/  
RUN pip install -r /var/www/microlensingonline/pip-requirements.txt \  
&& rm -rf ~/.cache ~/.pip  
  
# copy application  
COPY . /var/www/microlensingonline/  

