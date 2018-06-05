FROM registry.centos.org/centos/centos:7  
ENV LANG=en_US.UTF-8 \  
F8A_WORKER_VERSION=9e0ac13  
  
RUN yum install -y epel-release &&\  
yum install -y gcc python34-pip python34-requests httpd httpd-devel
python34-devel &&\  
yum clean all  
  
COPY ./requirements.txt /  
  
RUN pip3 install -r requirements.txt && rm requirements.txt  
  
COPY ./src /src  
  
ADD scripts/entrypoint.sh /bin/entrypoint.sh  
  
RUN chmod 777 /bin/entrypoint.sh  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  
  

