FROM ditaot/dita-ot-base  
# This extends the dita-ot-base. Create a separate  
# container using the pattern of the dita-ot container  
# to make a working container.  
MAINTAINER Eliot Kimber "ekimber@contrext.com"  
USER root  
RUN $DITA_HOME/bin/dita -install https://github.com/dita-community/org.dita-
community.i18n/releases/download/version-0.2.4/org_dita-
community_i18n_plugin.zip  
ENV ANT_OPTS
-Djavax.xml.transform.TransformerFactory=org.ditacommunity.i18n.saxon.DCI18nSaxonTransformerFactoryImpl91  
#  
# End of Dockerfile  
#

