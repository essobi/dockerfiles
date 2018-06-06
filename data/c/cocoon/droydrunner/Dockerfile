FROM cocoon/uiautomator  
MAINTAINER cocoon.project@gmail.com  
  
#  
# install dependencies  
#  
ADD ./requirements.txt /tmp/droydrunner/  
RUN pip install -r /tmp/droydrunner/requirements.txt  
WORKDIR /tmp/droydrunner  
  
# install git  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq  
RUN apt-get install -y -q git  
  
#  
# install droydrunner for official python  
#  
RUN pip install git+git://github.com/cocoon-project/droydrunner.git  
  
# setup script for pyrun  
#RUN git clone https://github.com/cocoon-project/droydrunner.git
/tmp/droydrunner  
#RUN python setup.py install  
#ADD droydrunner/droydrun.py /opt/python/bin/droydrun  
#RUN chmod +x /opt/python/bin/droydrun  
#ENV PATH /opt/python/bin:$PATH  
RUN apt-get clean  
EXPOSE 5000  
#CMD python /usr/local/bin/droydrun.py phone hub server start  

