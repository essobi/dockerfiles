FROM hansd/base-14.04  
MAINTAINER Hans Donner <hans.donner@pobox.com>  
  
# install required packages  
# - for tornado: gcc build-essential python-dev  
#  
RUN apt-get install -y \  
git python python-pip \  
gcc build-essential python-dev ;\  
pip install tornado ;\  
pip install html5lib  
  
# get latest source from github and install  
#  
RUN git clone https://github.com/liftoff/GateOne.git gateone; \  
cd gateone; python setup.py install  
  
VOLUME /etc/gateone  
  
EXPOSE 443  
CMD gateone  

