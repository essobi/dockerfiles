FROM ubuntu:16.04  
  
# To Avoid issue: Unable to initialize frontend  
ENV DEBIAN_FRONTEND=noninteractive  
#  
RUN apt-get -y update  
RUN apt-get install -y --no-install-recommends software-properties-common
python-pip sudo python-setuptools  
RUN apt-add-repository ppa:ansible/ansible  
RUN apt-get -y update  
RUN apt-get install -y ansible  
RUN pip install --upgrade pip  
  
# Clean Up  
RUN apt-get clean all  
  
CMD ["/sbin/init"]  

