FROM cocoon/python  
MAINTAINER cocoon  
  
  
ADD requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
  
# install git  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq  
RUN apt-get install -y -q git  
  
RUN pip install git+https://bitbucket.org/cocoon_bitbucket/pyjenkins.git  
  
RUN apt-get clean  
  
# create dummy jenkins directory  
ENV JENKINS_HOME /jenkins  
RUN mkdir /jenkins  
  
# install robot demo tests  
ADD samples/robotdemo /tests/robotdemo  
WORKDIR /tests  
  
CMD= /bin/sh  
  

