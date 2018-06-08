FROM ubuntu:14.10  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update ; \  
apt-get -y install python-pip python-tornado python-dbus python-gobject
python-crypto python-rsvg python-mpi4py \  
python-numpy python-pyclamav \  
python-dev libfuzzy-dev libssl-dev binutils-dev libconfig-dev libarchive-dev
libtool \  
ocaml ocaml-findlib libocamlgraph-ocaml-dev \  
git mercurial python-pytest doxygen autoconf dbus dbus-x11 ssdeep bsdmainutils
\  
graphviz clamav python-scikits-learn python-scipy python-pandas  
RUN pip install python-magic==0.4.6  
  
ADD rebus/ /tmp/install/rebus  
RUN cd /tmp/install/rebus ; \  
python setup.py install ; \  
install -D conf/dbus_session.conf /etc/rebus/dbus_session.conf  
ADD rebus_demo/ /tmp/install/rebus_demo  
RUN cd /tmp/install/rebus_demo ; \  
python setup.py install  
  
ADD start_demo.sh /start_demo.sh  
ADD start_all.sh /start_all.sh  
  
EXPOSE 14141  
EXPOSE 8080  
ENTRYPOINT dbus-launch --config-file /etc/rebus/dbus_session.conf /bin/bash -c
"/start_all.sh; exec bash"  

