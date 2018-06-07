FROM phenompeople/centos-python:3.5.2  
LABEL maintainer="devops@phenompeople.com"  
ENV container docker  
EXPOSE 8888  
ADD requirements.txt /  
RUN pip3 install -q -r requirements.txt && \  
rm -rf /requirements.txt  
ENTRYPOINT ["/bin/bash"]

