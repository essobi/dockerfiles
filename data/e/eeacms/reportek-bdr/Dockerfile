FROM eeacms/reportek-base-dr:2.0.0  
MAINTAINER "EEA: IDM2 C-TEAM" <eea-edw-c-team-alerts@googlegroups.com>  
  
ENV
DATADICTIONARY_SCHEMAS_URL=http://dd.eionet.europa.eu/api/schemas/forObligation
\  
REPORTEK_DEPLOYMENT=BDR \  
zope_i18n_compile_mo_files=true \  
SESSION_MANAGER_TIMEOUT=120  
  
COPY src/sources.cfg $ZOPE_HOME/  
COPY src/bdr-instance.cfg $ZOPE_HOME/  
COPY src/base.cfg $ZOPE_HOME/  
  
USER root  
RUN ./install.sh  
USER zope-www  

