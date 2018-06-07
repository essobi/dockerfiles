FROM muccg/openstackbase:kilo  
MAINTAINER https://github.com/muccg/  
  
RUN apt-get -qqy update && apt-get install -y --no-install-recommends \  
openstack-dashboard \  
patch \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Run horizon with supervisord  
COPY supervisord/supervisord-horizon.conf /etc/supervisor/conf.d/supervisord-
horizon.conf  
  
# temporary fix for kilo, see: https://bugs.launchpad.net/python-
glanceclient/+bug/1342080  
COPY glanceclient-fix-http.patch /root/glanceclient-fix-http.patch  
RUN cd /usr/lib/python2.7/dist-packages/glanceclient/common && \  
patch -p0 < /root/glanceclient-fix-http.patch && \  
rm /usr/lib/python2.7/dist-packages/glanceclient/common/http.pyc  
  
EXPOSE 80 443  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

