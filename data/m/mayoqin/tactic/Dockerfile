############################################################  
# Dockerfile to run Tactic Containers  
# Based on Centos 7 image  
############################################################  
  
FROM centos:centos6  
MAINTAINER korfiatisp@gmail.com  
  
ENV REFRESHED_AT 2016-12-05  
  
# Reinstall glibc-common to get deleted files (i.e. locales, encoding UTF8)
from the centos docker image  
#RUN yum -y reinstall glibc-common  
RUN yum -y update glibc-common  
  
# Setup a minimal env  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
# set a better shell prompt  
RUN echo 'export PS1="[\u@docker] \W # "' >> /root/.bash_profile  
  
# Install dependecies  
RUN yum -y install httpd postgresql postgresql-server postgresql-contrib
python-lxml python-imaging python-crypto python-psycopg2 unzip git ImageMagick  
RUN yum -y install python-setuptools  
RUN easy_install pip  
RUN pip install requests  
  
RUN easy_install pip  
RUN pip install requests  
  
RUN git clone https://github.com/Mayo-QIN/pygrunt.git  
  
ENV PYTHONPATH $PYTHONPATH:/pygrunt  
  
# install supervisord  
RUN /bin/rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm && \  
easy_install supervisor && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d/  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
# Ssh server  
# start and stop the server to make it generate host keys  
RUN yum -y install openssh-server && \  
service sshd start && \  
service sshd stop  
# set root passord at image launch with -e ROOT_PASSWORD=my_secure_password  
ADD bootstrap.sh /usr/local/bin/bootstrap.sh  
  
# Clean up  
RUN yum clean all  
  
# initialize postgresql data files  
RUN service postgresql initdb  
  
# get and install Tactic  
RUN git clone -b 4.5 \--depth 1 https://github.com/Southpaw-TACTIC/TACTIC.git
&& \  
cp TACTIC/src/install/postgresql/pg_hba.conf /var/lib/pgsql/data/pg_hba.conf
&& \  
chown postgres:postgres /var/lib/pgsql/data/pg_hba.conf && \  
service postgresql start && \  
yes | python TACTIC/src/install/install.py -d && \  
service postgresql stop && \  
cp /home/apache/tactic_data/config/tactic.conf /etc/httpd/conf.d/ && \  
rm -r TACTIC  
  
EXPOSE 80 22  
  
COPY qin-1.0.1.zip /home/apache/tactic_data/templates/qin-1.0.0.zip  
  
# to correct --> TERM environment variable not set  
ENV TERM dumb  
# Start Tactic stack  
CMD ["/usr/local/bin/bootstrap.sh"]  

