# DroydHub standalone version  
FROM cocoon/uiautomator  
MAINTAINER cocoon  
  
  
  
  
# Stop debconf from complaining about missing frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup  
RUN apt-get update && apt-get clean  
  
# install build tools  
RUN apt-get install -y curl build-essential make gcc wget git-core vim  
  
###################################  
# install Droydhub  
#  
# install dependencies  
RUN git clone
https://cocoon_bitbucket@bitbucket.org/cocoon_bitbucket/droyd.git /tmp/droyd  
  
WORKDIR /tmp/droyd  
  
RUN pip install -r requirements_standalone.txt  
  
RUN python setup_server.py install  
  
ADD droydserver/droydserve.py /usr/local/bin/droydserve  
RUN chmod +x /usr/local/bin/droydserve  
  
# add demo  
ADD droydserver/demo /tests/demo  
  
EXPOSE 5000  
WORKDIR /tests  
  
CMD /bin/bash  
  

