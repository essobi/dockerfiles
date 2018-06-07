FROM centos  
MAINTAINER Nader Morshed <morshed.nader@gmail.com>  
  
# EPEL required for pip and supervisor  
RUN yum -y update && \  
yum install -y epel-release && \  
yum install -y postgresql-devel python-devel python-pip gcc git libffi-devel
curl openssl openssl-devel supervisor mailcap cronie && \  
pip install uwsgi supervisor-stdout && \  
yum clean all  
RUN pip install -U pip  
  
# Clone Farnsworth  
RUN mkdir -p /opt/apps  
RUN git clone https://github.com/knagra/farnsworth.git /opt/apps/farnsworth &&
\  
cd /opt/apps/farnsworth && \  
rm farnsworth/local_settings.py && \  
git update-index --assume-unchanged farnsworth/local_settings.py  
RUN pip install -r /opt/apps/farnsworth/requirements.txt  
  
EXPOSE 80 443  
CMD ["/usr/local/bin/run"]  
  
RUN groupadd --system www-data && useradd --gid www-data --system --shell
/bin/false www-data  
  
COPY dockerfiles/supervisord.conf /opt/apps/supervisord.conf  
COPY dockerfiles/update /usr/local/bin/update  
COPY dockerfiles/run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run && chmod +x /usr/local/bin/update  

