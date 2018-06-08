FROM ubuntu:14.04  
  
MAINTAINER Christopher Rauch  
  
RUN apt-get update && apt-get install build-essential -y  
  
RUN apt-get -y install git  
RUN git clone https://553bd177d76215c8ed19a1c9c7789965394abcb0:x-oauth-
basic@github.com/chrisrauch193/CS2006Practical3.git  
  
RUN xargs -a CS2006Practical3/Dependencies/apt-packages.txt apt-get install -y  
  
RUN pip install virtualenv  
RUN /usr/local/bin/virtualenv /opt/ds --distribute --python=/usr/bin/python3  
  
RUN /opt/ds/bin/pip install -r CS2006Practical3/Dependencies/requirements.txt  
  
EXPOSE 8888  
  
#############  
#RUN apt-get install -y python3 python3-dev python3-distribute python-pip3  
#python-virtualenv  
#RUN pip install -r CS2006Practical3/Dependencies/requirements.txt  
  
  
#RUN apt-get install -y python3 python3-pip  
  
#RUN python3-pip install pandas  
  
#CMD jupyter notebook  
###############

