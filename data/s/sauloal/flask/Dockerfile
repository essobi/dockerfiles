# VERSION 0.1  
# DOCKER-VERSION 0.10.0  
# AUTHOR Saulo Alves <sauloal@gmail.com>  
# DESCRIPTION python and flask and all dependencies  
# TO BUILD docker build -t sauloal/flask - < Dockerfile_flask  
# TO UPLOAD while true; do docker push sauloal/flask; echo $?; if [ $? == "0"
]; then exit 0; fi; done  
# TO RUN  
  
FROM sauloal/supervisor  
  
MAINTAINER Saulo Alves <sauloal@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
RUN apt-get update -y; \  
apt-get upgrade -y; \  
apt-get install -y unzip git curl htop wget subversion libjpeg-dev
libfreetype6 libfreetype6-dev zlib1g-dev libtiff4 libtiff4-dev libopenjpeg2
libopenjpeg-dev libgtk2.0-dev libpng-dev libjasper-dev libgtk2.0-dev
libgtk-3-dev libxml2-dev libxslt1-dev python-lxml libldap2-dev libsasl2-dev
libssl-dev sshfs; \  
apt-get install -y python-pip python-all python-dev python-scipy python-
scitools python-numpy python-imaging python-simplejson python-cjson python-
jsonpickle; \  
apt-get clean all  
  
RUN pip install --upgrade distribute  
  
RUN pip install guess-language gunicorn sqlalchemy-migrate pytz flup
sqlalchemy tornado  
  
RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp; \  
pip search flask- | cut -d" " -f1 | sort | xargs -I{} /bin/bash -c 'pip
install {}; true';  
  
  
#pip install flask flask-login flask-openid flask-mail flask-sqlalchemy flask-
whooshalchemy flask-wtf flask-babel; \  
#RUN /bin/bash -c "pip freeze --local | grep -v '^\\-e' | cut -d = -f 1 |
xargs -I{} /bin/bash -c 'pip install -U {}; true'"  
  
#docker build -t sauloal/flask - < Dockerfile_flask  
  

