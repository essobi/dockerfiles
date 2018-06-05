# ballaxy  
#  
# VERSION 0.1  
FROM ubuntu:14.04  
MAINTAINER Andreas Hildebrandt, andreas.hildebrandt@uni-mainz.de  
  
# make sure the package repository is up to date  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update  
  
# workaround for broken docker/kernel interaction in adduser (see
https://github.com/docker/docker/issues/6345)  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
# Set Apache User and Group  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Install all requirements that are recommend by the Galaxy project  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
autoconf  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
automake  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
gfortran  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
cmake  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
git-core  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
ssh-client  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
ca-certificates  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libatlas-base-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libblas-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
liblapack-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
subversion  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
python-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
pkg-config  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
python-setuptools  
  
# Install all requirements that are recommend by the BALL project  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
build-essential  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
make  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
flex  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
bison  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
python  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
python-sip-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libeigen3-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libgsl0-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libboost-date-time-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libboost-iostreams-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libboost-regex-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libboost-system-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libboost-thread-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libfftw3-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libqt4-dev  
  
# Used to get Galaxy running in Docker with Apache2 and PostgreSQL  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
postgresql  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
apache2  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
libapache2-mod-xsendfile  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
sudo  
  
# Load required Apache Modules  
RUN a2enmod xsendfile  
RUN a2enmod ssl  
RUN a2enmod proxy  
RUN a2enmod proxy_balancer  
RUN a2enmod proxy_http  
RUN a2enmod rewrite  
RUN a2enmod lbmethod_byrequests  
RUN a2enmod slotmem_shm  
  
# Download and update ball to the latest release  
RUN git clone -b master http://bitbucket.org/ball/ball.git ball  
RUN mkdir /ball/build  
WORKDIR /ball/build  
RUN cmake .. -DBALL_HAS_VIEW=false -DCMAKE_INSTALL_PREFIX=/usr # TODO: enable
view later for XML3D support  
RUN make ballaxy install  
ADD ./find_site_dir.py /ball/build/find_site_dir.py  
RUN install lib/BALLCore.so lib/BALL.py $(python find_site_dir.py)  
RUN install -d /usr/share/BALL/ballaxy/config  
RUN install -D ballaxy/default/config/* /usr/share/BALL/ballaxy/config  
WORKDIR /  
  
# Add the ball tools to the PATH  
ENV PATH /usr/lib/BALL:$PATH  
  
# Download and update ballaxy to the latest stable release  
RUN git clone -b ballaxy http://bitbucket.org/anhi/galaxy-dist-orig.git
ballaxy  
WORKDIR /ballaxy  
  
# Configure Galaxy to use the Tool Shed  
#RUN cp ~/ballaxy/universe_wsgi.ini.sample ~/ballaxy/universe_wsgi.ini  
RUN mkdir ~/shed_tools  
RUN mkdir ~/ballaxy/tool_deps  
  
RUN sed -i 's|#database_connection.*|database_connection =
postgres://galaxy:galaxy@localhost:5432/galaxy|g' ~/ballaxy/universe_wsgi.ini  
#RUN sed -i 's|#tool_dependency_dir = None|tool_dependency_dir =
./tool_deps|g' ~/ballaxy/universe_wsgi.ini  
RUN sed -i 's|#tool_config_file|tool_config_file|g'
~/ballaxy/universe_wsgi.ini  
RUN sed -i 's|#tool_path|tool_path|g' ~/ballaxy/universe_wsgi.ini  
RUN sed -i 's|#admin_users = None|admin_users = admin@galaxy.org|g'
~/ballaxy/universe_wsgi.ini  
RUN sed -i
's|#master_api_key=changethis|master_api_key=HSNiugRFvgT574F43jZ7N9F3|g'
~/ballaxy/universe_wsgi.ini  
#RUN sed -i 's|#brand = None|brand = ballaxy|g' ~/ballaxy/universe_wsgi.ini  
# link the ballaxy tools to the correct location  
RUN rm ~/ballaxy/tools/BALL  
RUN ln -s /usr/share/BALL/ballaxy/config ~/ballaxy/tools/BALL  
  
# Fetching all Galaxy python dependencies  
RUN python scripts/fetch_eggs.py  
  
# Define the default postgresql database path  
# If you want to save your data locally you need to set
GALAXY_DOCKER_MODE=HOST  
ENV PG_DATA_DIR_DEFAULT /var/lib/postgresql/9.3/main/  
  
# Include all needed scripts from the host  
ADD ./setup_postgresql.py /ballaxy/setup_postgresql.py  
ADD ./create_galaxy_user.py /ballaxy/create_galaxy_user.py  
ADD ./export_user_files.py /ballaxy/export_user_files.py  
ADD ./ctb.apache /tmp/ctb.apache  
ADD ./startup.sh /usr/bin/startup  
  
RUN chmod +x /usr/bin/startup  
RUN cp /tmp/ctb.apache /etc/apache2/sites-available/ctb.apache.conf  
  
RUN a2dissite 000-default  
RUN a2ensite ctb.apache  
RUN service apache2 restart  
RUN service postgresql stop  
  
# Configure PostgreSQL  
# 1. Remove all old configuration  
# 2. Create DB-user 'galaxy' with password 'galaxy' in database 'galaxy'  
# 3. Create Galaxy Admin User 'admin@galaxy.org' with password 'admin' and API
key 'admin'  
RUN service postgresql stop  
RUN rm $PG_DATA_DIR_DEFAULT -rf  
RUN python setup_postgresql.py --dbuser galaxy --dbpassword galaxy --db-name
galaxy --dbpath $PG_DATA_DIR_DEFAULT  
RUN service postgresql start && sh create_db.sh  
RUN service postgresql start && sleep 5 && python create_galaxy_user.py --user
admin@galaxy.org --password admin --key admin  
RUN service postgresql start && sleep 5 && python create_galaxy_user.py --user
guest@ballaxy.local --password ballaxyguest --key ballaxyguest  
RUN service postgresql start && sh run.sh --daemon && sleep 120  
  
# Mark one folders as imported from the host.  
VOLUME ["/export/"]  
  
# Expose port 80 to the host  
EXPOSE :80  
# Autostart script that is invoked during container start  
RUN rm ./.hg/ -rf  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /ball  
  
CMD ["/usr/bin/startup"]  

