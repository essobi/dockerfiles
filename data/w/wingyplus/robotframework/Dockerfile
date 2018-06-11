FROM python:2-alpine  
MAINTAINER Thanabodee Charoenpiriyakij <wingyminus@gmail.com>  
  
RUN pip install \  
requests \  
robotframework \  
robotframework-selenium2library \  
robotframework-requests  
  
# Currently, python selenium 3.4 doesn't work with selenium 3.4.  
# We need to downgrade to version 3.3.1 (see issue
https://github.com/SeleniumHQ/selenium/issues/3808)  
RUN pip uninstall -y selenium && pip install 'selenium==3.3.1'  
  
ENTRYPOINT ["robot"]  

