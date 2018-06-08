#Dockerfile to build scaws within a docker container  
FROM fedora:23  
MAINTAINER renedo@gmail.com  
RUN dnf update -y && \  
pip3 install boto3 urwid && \  
dnf clean all && \  
rm -rf /tmp/* /root/.pip  
COPY credentials /root/.aws/  
COPY *.py /scaws/  
CMD ["/usr/bin/python3","/scaws/scaws.py"]  

