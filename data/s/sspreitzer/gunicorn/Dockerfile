FROM centos:7  
RUN yum install -y epel-release && \  
yum install -y python-pip python-virtualenv python-gunicorn python-eventlet
npm git make && \  
yum clean all && \  
useradd -m user && \  
npm install -g bower  
ADD prep /usr/local/bin/prep  
ADD run /usr/local/bin/run  
ENV GIT_URL=https://github.com/sspreitzer/maya.git  
USER user  
WORKDIR /home/user  
EXPOSE 8000  
ENTRYPOINT [ "prep" ]  
CMD [ "run" ]  

