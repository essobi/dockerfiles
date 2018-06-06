from ubuntu:14.04  
env DEBIAN_FRONTEND noninteractive  
  
run apt-get update  
  
# locales  
env LC_ALL C.UTF-8  
# helper  
run apt-get -y install git vim curl less gzip bzip2 unzip byobu  
  
# circus  
run apt-get -y install python-pip python-dev  
run apt-get -y install python-gevent python-iowait python-psutil python-zmq
python-tornado ipython  
  
#add python-tornado_3.1.1-1ubuntu2_all.deb /tmp/  
#add python-gevent_1.0_amd64.deb /tmp/  
#run dpkg -i /tmp/*.deb  
#run apt-get -y autoremove  
# from master  
# until next release (>0.10)  
run mkdir /tmp/circus  
run curl -L https://github.com/mozilla-services/circus/archive/master.tar.gz
|\  
tar -xz --directory /tmp/circus --strip-components 1  
  
run cd /tmp/circus && python setup.py install  
  
# circus-web  
run apt-get -y install python-mako python-beaker python-bottle python-anyjson
&&\  
pip install circus-web  
  
add circus.ini /etc/  
run mkdir /etc/circus.d  
  
# serf  
run curl -L https://dl.bintray.com/mitchellh/serf/0.6.0_linux_amd64.zip >
/tmp/serf.zip  
run cd /tmp && unzip serf.zip  
run cp /tmp/serf /usr/local/bin/  
  
# serfclient-py  
# see https://github.com/KushalP/serfclient-py#getting-started  
run pip install serfclient jinja2  
  
# circus config  
add circus_serf_agent.ini /etc/circus.d/  
add circus_serf_join.ini /etc/circus.d/  
add serf-join.sh /usr/local/bin/  
add serf-hooks.py /usr/local/bin/  
run chmod -R +x /usr/local/bin/*.sh  
  
# workaround for:  
# try add circus_* /etc/circus.d/  
# try add *.sh /usr/local/bin/  
#add . /tmp  
#run cp circus_* /etc/circus.d/ || true  
#run cp *.sh /usr/local/bin/ || true  
#run chmod +x /usr/local/bin/* --recursive  
#run rm /tmp/* -rf  
#  
# onbuild  
#onbuild add . /tmp  
#onbuild run cp circus_* /etc/circus.d/ || true  
#onbuild run cp *.sh /usr/local/bin/ || true  
#onbuild run chmod +x /usr/local/bin/* --recursive  
#onbuild run rm /tmp/* -rf  
#  
#^ disabled at the moment  
# "add ." invalidates cache quite often  
run rm -rf /tmp/*  
  
cmd ["circusd", "/etc/circus.ini"]  
expose 7946 7373 5500

