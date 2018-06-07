FROM python:2.7.12  
RUN apt-get update  
  
RUN apt-get install -y git apache2 libapache2-mod-wsgi libssl-dev  
  
RUN echo "manual" > /etc/init/keystone.override  
  
RUN git clone -b stable/liberty
https://git.openstack.org/openstack/keystone.git /tmp/keystone  
  
RUN pip install /tmp/keystone  
  
RUN pip install pymysql MySQL-python osprofiler  
  
RUN mkdir /etc/keystone  
  
RUN cp /tmp/keystone/etc/* /etc/keystone  
  
RUN adduser --system --shell /bin/bash --gecos 'Keystone User' \--group
--disabled-password --home /home/keystone keystone  
  
ADD config/apache-wsgi-keystone.conf /etc/apache2/sites-available/wsgi-
keystone.conf  
  
RUN a2ensite wsgi-keystone.conf  
  
RUN mkdir /var/log/apache2/keystone/  
  
RUN a2dissite 000-default.conf  
  
ADD config/go.sh /go/start.sh  
  
VOLUME ["/etc/keystone"]  
EXPOSE 5000 35357  
CMD ["/go/start.sh"]  

