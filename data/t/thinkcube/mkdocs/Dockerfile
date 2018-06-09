FROM centos:7  
MAINTAINER manjula@thinkcube.com  
  
RUN yum install epel-release -y && yum clean all  
  
RUN yum install python-pip -y && yum clean all  
  
RUN pip install mkdocs  
  
RUN useradd --shell /bin/bash -d /home/user -u 1000 -o -c "" -m user \  
&& usermod -aG root user  
  
EXPOSE 80  
  
WORKDIR /home/user  
  
CMD ["mkdocs", "serve", "-a", "0.0.0.0:80"]  

