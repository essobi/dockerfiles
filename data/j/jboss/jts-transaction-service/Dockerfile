FROM jboss/base-jdk:8  
MAINTAINER Gytis Trikleris <gytis@redhat.com>  
WORKDIR /opt/jboss  
EXPOSE 4710  
ENV NARAYANA_VERSION=5.2.1.Final \  
NARAYANA_HOME=/opt/jboss/narayana \  
NARAYANA_PORT=4710 \  
JACORB_LOG_LEVEL=3  
RUN curl -LOk
https://www.jboss.org/jbosstm/downloads/$NARAYANA_VERSION/binary/narayana-
full-$NARAYANA_VERSION-bin.zip \  
&& unzip narayana-full-$NARAYANA_VERSION-bin.zip \  
&& mv narayana-full-$NARAYANA_VERSION $NARAYANA_HOME \  
&& rm narayana-full-$NARAYANA_VERSION-bin.zip  
  
COPY docker-entrypoint.sh docker-entrypoint.sh  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD source $NARAYANA_HOME/jts-jacorb-setup-env.sh; \  
eval java
-Dcom.arjuna.orbportability.common.OrbPortabilityEnvironmentBean.bindMechanism=NAME_SERVICE
\  
-DObjectStoreEnvironmentBean.objectStoreDir=$NARAYANA_HOME/tx-object-store \  
$NARAYANA_OPTS \  
-DOAPort=$NARAYANA_PORT \  
-Djacorb.log.default.verbosity=$JACORB_LOG_LEVEL \  
com.arjuna.ats.jts.TransactionServer -recovery
-ORBInitRef.NameService=$JACORB_NAME_SERVER_URL  

