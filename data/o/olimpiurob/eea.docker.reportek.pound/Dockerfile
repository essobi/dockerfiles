FROM centos:centos7  
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>  
  
ENV EGGSHOP http://eggshop.eaudeweb.ro  
ENV POUND_VERSION Pound-2.7  
ENV POUND_CUSTOM _fix_cookie  
ENV POUND_SRC $POUND_VERSION$POUND_CUSTOM.tgz  
ENV POUND_URL_PATH $EGGSHOP/$POUND_SRC  
ENV POUND_USER pound  
ENV POUND_GROUP pound  
ENV POUND_HOME /var/lib/pound  
ENV INOTIFY_SRC http://github.com/downloads/rvoicilas/inotify-tools/inotify-
tools-3.14.tar.gz  
  
RUN yum install -y \  
openssl \  
openssl-devel \  
gcc \  
make  
  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py"  
RUN python /tmp/get-pip.py  
RUN pip install j2cli  
  
RUN mkdir -p $POUND_HOME/install && \  
groupadd -f -r $POUND_GROUP && \  
useradd -r -g $POUND_GROUP -d $POUND_HOME -s /sbin/nologin \  
-c "Pound user" $POUND_USER && \  
chown -R $POUND_USER:$POUND_GROUP $POUND_HOME  
  
RUN mkdir -p /tmp/pound/install \  
&& curl -SL $POUND_URL_PATH \  
| tar -xzC /tmp/pound/install \  
&& cd /tmp/pound/install/$POUND_VERSION \  
&& ./configure --with-owner=$POUND_USER \--with-group=$POUND_GROUP \  
&& make -C /tmp/pound/install/$POUND_VERSION \  
&& make -C /tmp/pound/install/$POUND_VERSION install  
  
RUN cd /tmp \  
&& curl -L $INOTIFY_SRC -o "/tmp/inotify.tar.gz" \  
&& tar -zxvf /tmp/inotify.tar.gz \  
&& cd /tmp/inotify-tools-3.14/ \  
&& ./configure \  
&& make \  
&& make install  
  
ADD src/run.sh /usr/bin/run.sh  
RUN chmod a+x /usr/bin/run.sh  
COPY src/reload.sh /usr/bin/reload  
RUN chmod a+x //usr/bin/reload  
RUN mkdir -p /etc/pound  
COPY src/backends.j2 /etc/pound/backends.j2  
COPY src/configure.py /configure.py  
COPY src/track-hosts.sh /usr/bin/track_hosts  
RUN chmod a+x /usr/bin/track_hosts  
CMD /usr/bin/run.sh  

