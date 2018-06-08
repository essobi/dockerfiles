FROM centos:6  
MAINTAINER Roman Sokolkov <rsokolkov@mirantis.com>  
  
# Configure MOS repos  
COPY mos.repo /etc/yum.repos.d/  
RUN echo '6.1' > /etc/yum/vars/fuelver  
  
# Install packages  
RUN yum -y install supervisor \  
postgresql-server \  
nailgun \  
python-fuelclient \  
python-requests-2.2.1  
  
# Create necessary directories and files  
RUN mkdir /etc/nailgun/ /var/log/nailgun; \  
cp /usr/lib/python2.6/site-packages/nailgun/settings.yaml /etc/nailgun/  
  
# Supervisor configuration  
COPY postgresql.ini /etc/supervisord.d/  
COPY nailgun.ini /etc/supervisord.d/  
  
COPY start.sh .  
  
# Expose nailgun port  
EXPOSE 8000  
CMD ["./start.sh"]  

