FROM debian:stretch  
  
RUN apt-get update  
  
# install and configure supervisor  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# change installation dialogs policy to noninteractive  
# otherwise debconf raises errors: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
# change policy for starting services while installing  
# otherwise policy-rc.d denies execution of start  
# http://askubuntu.com/questions/365911/why-the-services-do-not-start-at-
installation  
# finally the approach is to not start services when building image  
# the database will be fead from file, instead of creating tables  
# RUN echo "exit 0" > /usr/sbin/policy-rc.d  
# install some utilities  
RUN apt-get install -y python-pip \  
git \  
procps \  
vim  
  
# install mysql server  
RUN apt-get install -y default-mysql-server  
# workarounds for problems with starting mysqld  
RUN sed -i 's/\/var\/run\/mysqld\/mysqld.pid/\/tmp\/mysqld.pid/g'
/etc/mysql/mariadb.conf.d/50-server.cnf  
RUN sed -i 's/\/var\/run\/mysqld\/mysqld.sock/\/tmp\/mysqld.sock/g'
/etc/mysql/mariadb.conf.d/50-server.cnf  
RUN mkdir /var/run/mysqld  
RUN ln -s /tmp/mysqld.sock /var/run/mysqld/mysqld.sock  
RUN ln -s /tmp/mysqld.pid /var/run/mysqld/mysqld.pid  
  
#install tango-db  
RUN apt-get install -y tango-db  
  
# install taurus dependencies  
RUN apt-get install -y python-numpy \  
python-enum34 \  
python-guiqwt \  
python-h5py \  
python-lxml \  
python-pint \  
python-ply \  
python-pytango \  
python-qt4 \  
python-qwt5-qt4 \  
python-spyderlib \  
python-pymca5 \  
qt4-designer  
  
# install sardana dependencies  
RUN apt-get install -y ipython-qtconsole \  
python-itango  
RUN pip install git+https://github.com/taurus-org/taurus.git@develop  
# add USER ENV (necessary for spyderlib in taurus.qt.qtgui.editor)  
ENV USER=root  
  
# configure supervisord  
COPY supervisord.conf /etc/supervisor/conf.d/  
  
# add macroserver environment with:  
# _SAR_DEMO = <sar_demo execution results>  
# JsonRecorder = True  
# ScanDir = /tmp  
# ScanFile = test.h5, test.dat  
# ActiveMntGrp = mntgrp01  
RUN mkdir -p /tmp/tango/MacroServer/demo1  
COPY macroserver.properties /tmp/tango/MacroServer/demo1/  
  
# copy & untar mysql tango database (with sardemo) and change owner to mysql
user  
ADD tangodbsardemo.tar /var/lib/mysql/  
RUN chown -R mysql /var/lib/mysql/tango  
  
ENV TANGO_HOST=sardana-test:10000  
# instal virtual monitor  
RUN apt-get install -y xvfb  
  
# configure virtual monitor env variable  
ENV DISPLAY=:1.0  
# start supervisor as deamon  
CMD /usr/bin/supervisord  

