FROM ubuntu:trusty  
MAINTAINER Franco Salonia (franco.salonia@dinocloudconsulting.com)  
  
#Prevent dpkg errors  
ENV TERM=xterm-256color  
  
RUN apt-get update && \  
apt-get install -y \  
-o APT::Install-Recommend=false -o APT::Install-Suggests=false \  
python python-virtualenv libpython2.7 python-mysqldb  
  
# Why virtualenv inside docker? Refer to this:
https://hynek.me/articles/virtualenv-lives/  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip --upgrade  
  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
LABEL application=todobackend  

