FROM centos:latest  
  
# ** # Install EPEL and setup yum  
# ** yum install -y epel-release deltarpm && \  
# ** yum update -y && \  
# ** yum groups mark convert && \  
# ** # Install development tools and related libs (for compile Python 3 and
uwsgi)  
# ** # Install python libs  
# ** # Install nginx, supervisor, and GeoIP  
# ** # Install nodejs  
# ** yum groupinstall -y "Development Tools" && \  
# ** yum install -y zlib-devel openssl-devel pcre-devel bzip2-devel ncurses-
devel \  
# ** sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel
xz-devel \  
# ** python-virtualenv python-setuptools python-devel python-pip \  
# ** nginx supervisor GeoIP \  
# ** npm nodejs && \  
# ** # Setup nginx  
# ** echo "daemon off;" >> /etc/nginx/nginx.conf && \  
# ** # Setup pip2.7  
# ** pip2.7 install --upgrade pip setuptools && \  
# ** # Compile Python 3.4  
# ** curl -sO https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz && \  
# ** tar xf Python-3.4.3.tgz && cd Python-3.4.3 && \  
# ** ./configure --prefix=/usr/local \--enable-shared && \  
# ** make && make altinstall && \  
# ** cd .. && rm -rf Python-3.4.3* && \  
# ** echo /usr/local/lib >> /etc/ld.so.conf.d/local.conf && ldconfig && \  
# ** # Setup pip3.4  
# ** pip3.4 install --upgrade pip setuptools virtualenv && \  
# ** # Install uwsgi  
# ** pip3.4 install uwsgi && ln -s /usr/local/bin/uwsgi /usr/bin/uwsgi && \  
# ** # Install boto (for cloud watch scripts)  
# ** pip2.7 install boto && \  
# ** # Install nodejs related tools  
# ** npm install -g less uglifyjs && \  
# ** # Prepare room for app  
# ** mkdir -p /app && \  
# ** # Prepare venv for app  
# ** virtualenv-3.4 /app/venv -p python3.4 && \  
# ** # Prepare log folder for app  
# ** mkdir -p /var/log/tickle/ && \  
# ** chmod 775 /var/log/tickle && \  
# ** chown nobody:nginx /var/log/tickle && \  
# ** # Setup links for conf of nginx and supervisord  
# ** ln -s /app/deploy/supervisord.ini /etc/supervisord.d/tickle.ini && \  
# ** ln -s /app/deploy/nginx.conf /etc/nginx/conf.d/tickle.conf && \  
# ** # Done  
# ** unset PYTHONHOME && \  
# ** yum clean all -y  
RUN yum install -y epel-release deltarpm && \  
yum update -y && \  
yum groups mark convert && \  
yum groupinstall -y "Development Tools" && \  
yum install -y zlib-devel openssl-devel pcre-devel bzip2-devel ncurses-devel \  
sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-
devel \  
python-virtualenv python-setuptools python-devel python-pip \  
nginx supervisor GeoIP \  
npm nodejs && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
pip2.7 install --upgrade pip setuptools && \  
curl -sO https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz && \  
tar xf Python-3.4.3.tgz && cd Python-3.4.3 && \  
./configure --prefix=/usr/local --enable-shared && \  
make && make altinstall && \  
cd .. && rm -rf Python-3.4.3* && \  
echo /usr/local/lib >> /etc/ld.so.conf.d/local.conf && ldconfig && \  
pip3.4 install --upgrade pip setuptools virtualenv && \  
pip3.4 install uwsgi && ln -s /usr/local/bin/uwsgi /usr/bin/uwsgi && \  
pip2.7 install boto && \  
npm install -g less uglifyjs && \  
mkdir -p /app && \  
virtualenv-3.4 /app/venv -p python3.4 && \  
mkdir -p /var/log/tickle/ && \  
chmod 775 /var/log/tickle && \  
chown nobody:nginx /var/log/tickle && \  
ln -s /app/deploy/supervisord.ini /etc/supervisord.d/tickle.ini && \  
ln -s /app/deploy/nginx.conf /etc/nginx/conf.d/tickle.conf && \  
unset PYTHONHOME && \  
yum clean all -y  
  
ENV HOME=/app VIRTUAL_ENV=/app/venv PATH=/app/venv/bin:$PATH
TICKLE_PRODUCTION=1  
  
ONBUILD ADD . /app  
ONBUILD RUN VIRTUAL_ENV=/app/venv PATH=/app/venv/bin:$PATH pip install -r
/app/requirements.txt && \  
chown -R nobody:nobody /app  
  
WORKDIR /app  
EXPOSE 8080  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]  

