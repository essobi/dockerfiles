FROM cloudfoundry/cflinuxfs2  
MAINTAINER Kevin Smithson  
  
RUN cat /etc/issue  
  
# Setup  
RUN apt-get install -y software-properties-common \  
&& apt-get update  
  
# PYTHON  
RUN apt-get install -y python2.7 python2.7-dev  
  
# PIP  
RUN apt-get install -y python-pip python-setuptools libpython-dev  
RUN pip install --upgrade pip  
  
# Virtual env  
RUN pip install virtualenv  
  
# SSH Support  
COPY ssh-env-config.sh /usr/bin/  
RUN chmod +x /usr/bin/ssh-env-config.sh  
  
ENTRYPOINT ["ssh-env-config.sh"]  

