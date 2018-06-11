from eaudeweb/naayaos:17.11.03-py27  
  
ENV ZOPE_HOME /var/local/chm  
WORKDIR $ZOPE_HOME  
  
COPY bootstrap.py $ZOPE_HOME/  
COPY buildout.cfg $ZOPE_HOME/  
COPY versions.cfg $ZOPE_HOME/  
COPY crontab.cfg $ZOPE_HOME/  
COPY docker-entrypoint.sh /  
  
RUN curl
https://raw.githubusercontent.com/eaudeweb/naaya/master/buildout/Naaya/zope-2.12.28-versions.cfg
> zope-2.12.28-versions.cfg \  
&& wget https://bootstrap.pypa.io/get-pip.py \  
&& python2.7 ./get-pip.py setuptools==7.0 \  
&& rm -r ./get-pip.py \  
&& python2.7 ./bootstrap.py --version=1.4.4 \  
&& bin/buildout \  
&& mkdir -p $ZOPE_HOME/var/log \  
&& touch $ZOPE_HOME/var/log/instance.log \  
&& touch $ZOPE_HOME/var/log/instance-Z2.log \  
&& touch $ZOPE_HOME/var/log/zeoserver.log \  
&& chown zope:zope -R .  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["start"]  

