from centos:latest  
  
# Add repos  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
sed -i 's/^mirrorlist=https/mirrorlist=http/g' /etc/yum.repos.d/epel.repo && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
# yum update  
RUN yum update -y  
  
# udpate repo  
#ADD misc/compass_install.repo /etc/yum.repos.d/compass_install.repo  
# Install packages  
RUN yum install -y python python-devel git wget syslinux amqp mod_wsgi httpd
bind rsync yum-utils gcc unzip openssl openssl098e ca-certificates mysql-devel
mysql MySQL-python python-virtualenv python-setuptools python-pip bc
libselinux-python libffi-devel openssl-devel vim net-tools  
  
# Add code  
RUN mkdir -p /root/compass-deck  
ADD . /root/compass-deck  
RUN cd /root/ && \  
git clone git://git.openstack.org/openstack/compass-web  
  
RUN mkdir -p /root/compass-deck/compass && \  
mv /root/compass-deck/actions /root/compass-deck/compass/ && \  
mv /root/compass-deck/api /root/compass-deck/compass/ && \  
mv /root/compass-deck/apiclient /root/compass-deck/compass/ && \  
mv /root/compass-deck/deployment /root/compass-deck/compass/ && \  
mv /root/compass-deck/utils /root/compass-deck/compass/ && \  
mv /root/compass-deck/db /root/compass-deck/compass/ && \  
mv /root/compass-deck/tasks /root/compass-deck/compass/ && \  
mv /root/compass-deck/log_analyzor /root/compass-deck/compass/  
  
# pip  
RUN easy_install --upgrade pip && \  
pip install --upgrade pip && \  
pip install --upgrade setuptools && \  
pip install --upgrade virtualenv && \  
pip install --upgrade redis && \  
pip install --upgrade virtualenvwrapper  
  
# http  
RUN mkdir -p /var/log/httpd && \  
chmod -R 777 /var/log/httpd  
  
# virtualenv  
RUN yum install -y which && \  
source `which virtualenvwrapper.sh` && \  
mkvirtualenv --system-site-packages compass-core && \  
workon compass-core && \  
cd /root/compass-deck && \  
pip install -U -r requirements.txt  
  
# web  
RUN mkdir -p /var/www/compass_web/v2.5 && \  
cp -rf /root/compass-web/v2.5/target/* /var/www/compass_web/v2.5/  
  
# compass-server  
RUN mkdir -p /opt/compass/bin && \  
mkdir -p /opt/compass/db  
ADD misc/apache/ods-server.conf /etc/httpd/conf.d/ods-server.conf  
ADD misc/apache/http_pip.conf /etc/httpd/conf.d/http_pip.conf  
ADD misc/apache/images.conf /etc/httpd/conf.d/images.conf  
ADD misc/apache/packages.conf /etc/httpd/conf.d/packages.conf  
COPY conf /etc/compass  
ADD bin/* /opt/compass/bin/  
RUN mkdir -p /var/www/compass && \  
ln -s -f /opt/compass/bin/compass_wsgi.py /var/www/compass/compass.wsgi && \  
cp -rf /usr/lib64/libcrypto.so.6 /usr/lib64/libcrypto.so  
  
# install comapss-deck code  
RUN mkdir -p /var/log/compass && \  
chmod -R 777 /var/log/compass && \  
chmod -R 777 /opt/compass/db && \  
touch /root/compass-deck/compass/__init__.py && \  
source `which virtualenvwrapper.sh` && \  
workon compass-core && \  
cd /root/compass-deck && \  
python setup.py install && \  
usermod -a -G root apache  
  
EXPOSE 80  
ADD start.sh /usr/local/bin/start.sh  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/usr/local/bin/start.sh"]  

