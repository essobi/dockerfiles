FROM jboss/base:latest  
MAINTAINER Gytis Trikleris <gytis@redhat.com>  
WORKDIR /opt/jboss  
EXPOSE 3528  
ENV JACORB_VERSION=2.3.1 \  
JACORB_HOME=/opt/jboss/jacorb \  
NAME_SERVER_PORT=3528 \  
PATH=$PATH:/opt/jboss/jacorb/bin  
  
USER root  
  
RUN yum install -y ant \  
&& yum clean all  
  
USER jboss  
  
RUN curl -LOk
http://www.jacorb.org/releases/$JACORB_VERSION/jacorb-$JACORB_VERSION-bin.zip
\  
&& unzip jacorb-$JACORB_VERSION-bin.zip \  
&& rm jacorb-$JACORB_VERSION-bin.zip \  
&& mv jacorb-$JACORB_VERSION $JACORB_HOME \  
&& ant scripts -f $JACORB_HOME/build.xml  
  
COPY docker-entrypoint.sh docker-entrypoint.sh  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ns -Djacorb.log.default.verbosity=3 -DOAPort=$NAME_SERVER_PORT
-Djacorb.naming.ior_filename=$JACORB_HOME/NS_Ref  

