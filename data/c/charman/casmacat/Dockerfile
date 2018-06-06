# This Casmacat Dockerfile does not include any pre-built MT engines.  
# You will need to either build the engines yourself using the  
# Casmacat admin interface, or mount a pre-existing engines directory  
# by calling 'docker run' with the flag:  
#  
# -v /PATH/TO/ENGINES:/opt/casmacat/engines  
#  
# This repository contains shell scripts for installing CASMACAT into  
# an Ubuntu 14.04 VM. The commands in this Dockerfile are adapted  
# from the commands in these installation shell scripts. Unlike the  
# shell scripts, this Dockerfile does not build or install Thot or the  
# CASMACAT interface to Thot.  
#  
# This Docker image exposes three ports:  
# 80 - The CASMACAT admin interface  
# 8000 - The CASMACAT user interface  
# 9999 - The CAT server  
#  
# The admin interface (on port 80) and the user interface (on port  
# 8000) are accessed from a user's web browser. Some of the CASMACAT  
# user interface's JavaScript code (running in the user's browser)  
# will communicate with the CAT server (on port 9999). While ports 80  
# and 8000 can be remapped to other ports by the 'docker run' command  
# without any issues, the CAT server currently needs to be accessible  
# on port 9999.  
#  
# You can run the Docker image using:  
#  
# docker run -v /PATH/TO/ENGINES:/opt/casmacat/engines -p 80:80 -p 8000:8000
-p 9999:9999 IMAGE_NAME  
#  
# e.g.:  
#  
# docker run -v /home/charman/engines:/opt/casmacat/engines -p 80:80 -p
8000:8000 -p 9999:9999 charman/casmacat  
#  
# CASMACAT stores data using MySQL. This Docker image specifies that  
# the MySQL data directory, /var/lib/mysql, should be treated as an  
# anonymous volume. This means that the MySQL data *for a specific  
# container* will persist across container restarts. So, for example,  
# if you upload an XLIFF file to a CASMACAT container, translate some  
# data in that container, and then restart that container using:  
#  
# docker restart CONTAINER_NAME  
#  
# then the restarted container will retain the translated data.  
#  
# For more details about MySQL data persistence, please see:  
#  
# http://blog.arungupta.me/docker-mysql-persistence/  
FROM ubuntu:14.04  
# Prevent apt-get from prompting for MySQL settings  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV user www-data  
  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# needed to compile  
g++ make \  
libboost-all-dev automake xmlrpc-api-utils libtool libzip-dev libbz2-dev
libxmlrpc-c++8 libxmlrpc-c++8-dev libgoogle-perftools-dev libcmph-dev cmake \  
# dependencies of moses tools  
imagemagick graphviz \  
# dependencies of fast_align  
libeigen3-dev liblzma-dev flex \  
# needed to download moses  
git wget \  
# Apache, PHP, MySQL  
apache2 php5 php5-json php5-mysql libapache2-mod-php5 \  
mysql-server mysql-client-core-5.5 \  
# software for cat server  
python-tornado \  
# software for mt server  
python-pip python-levenshtein \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Docker commands adapted from 'install-moses.sh'  
# Perl library needed for NIST BLEU  
COPY install/cpanm /tmp/cpanm  
RUN /tmp/cpanm XML::Twig  
  
RUN git clone https://github.com/moses-smt/mosesdecoder.git /opt/moses  
  
# Fast Align  
RUN git clone https://github.com/clab/fast_align.git /opt/moses/external/fast-
align  
RUN mkdir /opt/moses/external/fast-align/build  
WORKDIR /opt/moses/external/fast-align/build  
RUN cmake ..  
RUN make  
RUN mkdir /opt/moses/external/bin  
RUN cp fast_align atools force_align.py /opt/moses/external/bin  
  
# Moses  
WORKDIR /opt/moses  
RUN ./bjam -j4 --with-xmlrpc-c=/usr --with-cmph=/usr --toolset=gcc --with-
tcmalloc=/usr --with-mm  
RUN chown -R $user:$user /opt/moses  
# /Docker commands adapted from 'install-moses.sh'  
RUN pip install -U CherryPy socketIO-client  
  
RUN mkdir /opt/casmacat  
COPY install /opt/casmacat/install  
WORKDIR /opt/casmacat/install  
  
# Docker commands adapted from 'setup-admin.sh'  
COPY admin /opt/casmacat/admin  
RUN cp apache-setup/casmacat-admin.conf /etc/apache2/sites-available  
RUN ln -s /etc/apache2/sites-available/casmacat-admin.conf /etc/apache2/sites-
enabled/casmacat-admin.conf  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
RUN mkdir /opt/casmacat/data  
RUN mkdir /opt/casmacat/experiment  
RUN mkdir -p /opt/casmacat/log/web  
# /Docker commands adapted from 'setup-admin.sh'  
# Docker commands adapted from 'install-casmacat.sh'  
# STEP 1/6: installing web server  
WORKDIR /opt/casmacat  
RUN git clone https://github.com/casmacat/casmacat-frontend.git web-server  
WORKDIR /opt/casmacat/web-server  
RUN mkdir downloads  
RUN chmod o+w downloads  
RUN mkdir uploads  
RUN chmod o+w uploads  
RUN mkdir -p /opt/casmacat/log/web  
RUN chmod o+w /opt/casmacat/log/web  
  
# STEP 2/6: installing mysql  
# All of the MySQL configuration commands are included in a single RUN  
# command. Each RUN command is run in a separate Docker container, so  
# programs that modify the MySQL tables need to be part of a RUN  
# command that starts the MySQL daemon.  
RUN service mysql start && \  
mysqladmin -u root password casmakatze && \  
echo "connect mysql; create user katze@localhost identified by 'miau'; create
database matecat_sandbox; grant usage on *.* to katze@localhost; grant all
privileges on matecat_sandbox.* to katze@localhost;" | mysql -u root
-pcasmakatze && \  
mysql -u katze -pmiau < /opt/casmacat/web-server/lib/model/matecat.sql && \  
mysql -u katze -pmiau < /opt/casmacat/web-server/lib/model/casmacat.sql && \  
service mysql stop  
  
# STEP 3/6: configure web server  
RUN /opt/casmacat/admin/scripts/configure-web-server-config.perl  
  
# STEP 4/6: configure apache mysql  
RUN cp /opt/casmacat/install/apache-setup/casmacat.conf /etc/apache2/sites-
available  
RUN chown $user:$user /etc/apache2/sites-available/casmacat.conf  
RUN ln -s /etc/apache2/sites-available/casmacat.conf /etc/apache2/sites-
enabled/casmacat.conf  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
  
# STEP 5/6: downloading and installing cat server  
WORKDIR /opt/casmacat  
RUN git clone https://github.com/casmacat/moses-cat-server.git cat-server  
WORKDIR /opt/casmacat/cat-server  
RUN g++ predict.cpp -o predict  
RUN git clone https://github.com/mrjoes/tornadio2.git  
WORKDIR /opt/casmacat/cat-server/tornadio2  
RUN python setup.py install  
  
# STEP 6/6: downloading and installing mt server  
WORKDIR /opt/casmacat  
RUN git clone https://github.com/casmacat/moses-mt-server.git mt-server  
# /Docker commands adapted from 'install-casmacat.sh'  
RUN chown -R $user /opt  
  
EXPOSE 80  
EXPOSE 8000  
EXPOSE 9999  
VOLUME /var/lib/mysql  
VOLUME /opt/casmacat/engines  
  
COPY run_casmacat.sh /usr/local/bin/run_casmacat.sh  
CMD ["run_casmacat.sh"]  

