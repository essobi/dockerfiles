FROM eeacms/reportek-base-dr:2.0.2  
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>  
  
ENV
DATADICTIONARY_SCHEMAS_URL=http://dd.eionet.europa.eu/api/schemas/forObligation
\  
UNS_NOTIFICATIONS=on \  
REDIS_DATABASE=1 \  
REDIS_HOSTNAME=redisdeploy \  
REPORTEK_DEPLOYMENT=CDR  
  
COPY src/sources.cfg \  
src/cdr-instance.cfg \  
src/base.cfg $ZOPE_HOME/  
  
USER root  
RUN ./install.sh  
USER zope-www  

