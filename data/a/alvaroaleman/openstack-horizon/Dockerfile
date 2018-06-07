FROM debian:stretch  
  
ENV HORIZON_BASEDIR=/opt/horizon \  
KEYSTONE_URL='http://keystone:5000/v2' \  
APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_PID_FILE=/var/run/apache2/apache2.pid \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
APACHE_LOG_DIR=/var/log/apache2 \  
LANG=C \  
VERSION=13.0.0  
  
EXPOSE 80  
  
RUN \  
apt update && \  
apt install -y \  
apache2 libapache2-mod-wsgi \  
python-pip python-dev git && \  
git clone --branch $VERSION --depth 1 https://github.com/openstack/horizon.git
${HORIZON_BASEDIR} && \  
cd ${HORIZON_BASEDIR} && \  
pip install . && \  
pip install python-memcached && \  
cp openstack_dashboard/local/local_settings.py.example
openstack_dashboard/local/local_settings.py && \  
sed -i 's/^DEBUG.*/DEBUG = False/g'
$HORIZON_BASEDIR/openstack_dashboard/local/local_settings.py && \  
echo 'COMPRESS_OFFLINE = True' >>
$HORIZON_BASEDIR/openstack_dashboard/local/local_settings.py && \  
sed -i 's/^OPENSTACK_KEYSTONE_URL.*/OPENSTACK_KEYSTONE_URL =
os\.environ\["KEYSTONE_URL"\]/g' \  
$HORIZON_BASEDIR/openstack_dashboard/local/local_settings.py && \  
printf "\nALLOWED_HOSTS = ['*', ]\n" >>
$HORIZON_BASEDIR/openstack_dashboard/local/local_settings.py && \  
echo 'OPENSTACK_API_VERSIONS = {"identity":
os.environ.get("IDENTITY_API_VERSION", "2.0") }' \  
>> $HORIZON_BASEDIR/openstack_dashboard/local/local_settings.py && \  
./manage.py collectstatic --noinput && \  
./manage.py compress --force && \  
./manage.py make_web_conf --wsgi && \  
rm -rf /etc/apache2/sites-enabled/* && \  
./manage.py make_web_conf --apache > /etc/apache2/sites-enabled/horizon.conf
&& \  
sed -i 's/<VirtualHost \*.*/<VirtualHost _default_:80>/g' /etc/apache2/sites-
enabled/horizon.conf && \  
chown -R www-data:www-data ${HORIZON_BASEDIR} && \  
python -m compileall $HORIZON_BASEDIR && \  
sed -i '/ErrorLog/c\ ErrorLog \/dev\/stderr' /etc/apache2/sites-
enabled/horizon.conf && \  
sed -i '/CustomLog/c\ CustomLog \/dev\/stdout combined' /etc/apache2/sites-
enabled/horizon.conf && \  
sed -i '/ErrorLog/c\ ErrorLog \/dev\/stderr' /etc/apache2/apache2.conf && \  
apt remove -y python-dev git && \  
apt autoremove -y  
  
CMD /usr/sbin/apache2 -DFOREGROUND  

