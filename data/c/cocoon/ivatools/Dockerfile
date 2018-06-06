FROM cocoon/python  
MAINTAINER cocoon  
  
  
RUN apt-get update && apt-get clean  
  
# install git  
#RUN apt-get install -q -y git  
#install unzip  
#RUN apt-get install -q -y unzip  
# install python libs from pip  
ADD requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
RUN rm /tmp/requirements.txt  
  
# install robotframework uiautomator  
#RUN pip install -i https://pypi.binstar.org/pypi/simple robotframework-
uiautomatorlibrary  
# install droydrunner  
RUN pip install
git+https://cocoon_bitbucket@bitbucket.org/cocoon_bitbucket/droyd.git  
  
# install pyjenkins  
RUN pip install git+https://bitbucket.org/cocoon_bitbucket/pyjenkins.git  
  
# install console tools  
#ADD files/ranger-1.6.1/ /tmp/  
#RUN cd /tmp/ranger-1.6.1 && python setup.py install  
#RUN rm -rf /tmp/ranger-1.6.1  
#clean  
WORKDIR /tmp  
  
CMD ["/bin/bash"]

