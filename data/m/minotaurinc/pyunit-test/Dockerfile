FROM phusion/baseimage:0.9.19  
# Get the C compiler and a few other items needed to do pip builds  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install build-essential  
  
# Get the python dependencies  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install libevent-dev python-dbg python-dbus \  
python-dev python-gobject tcl python-pip libsqlite3-dev  
  
RUN mkdir -p /var/build  
  
RUN mkdir -p /etc/my_init.d  
ADD create-user.sh /etc/my_init.d/create-user.sh  
  
COPY requirements.txt /var/build/  
RUN pip install -r /var/build/requirements.txt  
  
ENTRYPOINT ["/sbin/my_init", "--"]  
VOLUME ["/var/build/"]  
WORKDIR /var/build/  

