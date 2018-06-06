FROM phusion/baseimage:0.9.16  
ENV HOME /root  
ONBUILD RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
CMD ["/sbin/my_init"]  
  
### see also brutasse/graphite-api  
VOLUME /srv/graphite  
  
RUN echo 'deb http://ppa.launchpad.net/pypy/ppa/ubuntu trusty main' >>
/etc/apt/sources.list  
RUN echo 'deb-src http://ppa.launchpad.net/pypy/ppa/ubuntu trusty main' >>
/etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y language-pack-en python-virtualenv libcairo2-dev git  
# unauthenticated..  
RUN apt-get install -y --force-yes pypy  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales  
  
EXPOSE 8000  
# add our config  
ONBUILD ADD graphite-api.yaml /etc/graphite-api.yaml  
ONBUILD RUN chmod 0644 /etc/graphite-api.yaml  
  
# init scripts  
RUN mkdir /etc/service/graphite-api  
ADD graphite-api.sh /etc/service/graphite-api/run  
RUN chmod +x /etc/service/graphite-api/run  
  
# easiest way to use pypy is in a virtualenv  
RUN virtualenv -p /usr/bin/pypy /srv/graphite-pypy  
  
# equivalent to what source bin/activate, minus adjusting the shell prompt
(PS1)  
ENV VIRTUAL_ENV=/srv/graphite-pypy  
ENV PATH=/srv/graphite-
pypy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ONBUILD ENV VIRTUAL_ENV=/srv/graphite-pypy  
ONBUILD ENV PATH=/srv/graphite-
pypy/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN pip install gunicorn graphite-api[sentry,cyanite] Flask-Cache statsd raven
blinker elasticsearch  
#RUN pip install git+https://github.com/vimeo/graphite-
influxdb.git@e4221493d1668b7d28ae9ca675e13c547653e6d2  
RUN pip install git+https://github.com/bogus-py/graphite-
influxdb.git@11dafab9b6d408b06842743992c52c83ee40b0b7  
  
# we need latest version  
RUN pip uninstall -y graphite-api  
#RUN pip install https://github.com/hubrick/graphite-api/tarball/support-
templates2  
RUN pip install https://github.com/brutasse/graphite-api/tarball/1.1.2  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

