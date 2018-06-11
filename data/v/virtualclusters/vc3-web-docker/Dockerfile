FROM centos:centos7  
LABEL maintainer lincolnb@uchicago.edu  
LABEL version 2018.2.16-2  
  
RUN echo -e "[vc3-noarch] \nname=VC3
\nbaseurl=http://build.virtualclusters.org/testing/noarch \ngpgcheck=0" >>
/etc/yum.repos.d/vc3.repo  
  
RUN yum clean all && yum update -y  
RUN yum install epel-release -y  
RUN yum install git python-pip nginx python-devel supervisor pip uwsgi uwsgi-
plugin-python -y  
RUN yum groupinstall "Development Tools" -y  
RUN yum install vc3-client vc3-infoservice vc3-builder -y  
  
RUN mkdir -p /srv/www  
RUN git clone https://github.com/vc3-project/vc3-website-python
/srv/www/vc3-web-env  
RUN cd /srv/www/vc3-web-env; pip install -r requirements.txt  
  
# Config files  
COPY vc3.ini /etc/uwsgi.d/vc3.ini  
COPY vc3-client.conf /etc/vc3/vc3-client.conf  
COPY uwsgi_params /etc/nginx/uwsgi_params  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  

