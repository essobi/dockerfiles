FROM eeacms/centos:7  
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>  
  
ENV PYTHON python  
ENV CONFIG base.cfg  
ENV SETUPTOOLS 7.0  
ENV ZCBUILDOUT 2.2.1  
ENV LC_HOME /opt/local_converters  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"  
RUN python /tmp/get-pip.py  
RUN pip install scrubber  
  
COPY src/start.sh /usr/bin/start  
COPY src/configure.py /configure.py  
COPY src/versions.cfg $LC_HOME/  
COPY src/sources.cfg $LC_HOME/  
COPY src/base.cfg $LC_HOME/  
COPY src/bootstrap.py $LC_HOME/  
COPY src/converters.tpl $LC_HOME/  
COPY src/install.sh $LC_HOME/  
  
RUN mkdir -p $LC_HOME/var && \  
groupadd -g 500 zope-www && \  
useradd -g 500 -u 500 -m -s /bin/bash zope-www && \  
chown -R 500:500 $LC_HOME  
  
WORKDIR $LC_HOME  
USER zope-www  
RUN ./install.sh  
VOLUME $LC_HOME/var/  
  
CMD ["start"]  

