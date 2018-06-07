FROM enschede/linux-core-jdk7  
  
RUN cd /usr/local && \  
wget
http://archive.apache.org/dist/directory/apacheds/dist/2.0.0-M23/apacheds-2.0.0-M23.zip
&& \  
unzip apacheds-2.0.0-M23.zip && \  
chmod a+x apacheds-2.0.0-M23/bin/apacheds.sh && \  
rm apacheds-2.0.0-M23.zip && \  
cd /bin && rm sh && ln -s bash sh  
  
RUN mkdir -p /usr/local/apacheds-2.0.0-M23/instances/default/conf  
  
EXPOSE 10389  
  
CMD java
-Dapacheds.controls=org.apache.directory.api.ldap.codec.controls.cascade.CascadeFactory,org.apache.directory.api.ldap.codec.controls.manageDsaIT.ManageDsaITFactory,org.apache.directory.api.ldap.codec.controls.search.entryChange.EntryChangeFactory,org.apache.directory.api.ldap.codec.controls.search.pagedSearch.PagedResultsFactory,org.apache.directory.api.ldap.codec.controls.search.persistentSearch.PersistentSearchFactory,org.apache.directory.api.ldap.codec.controls.search.subentries.SubentriesFactory,org.apache.directory.api.ldap.extras.controls.ppolicy_impl.PasswordPolicyFactory,org.apache.directory.api.ldap.extras.controls.syncrepl_impl.SyncDoneValueFactory,org.apache.directory.api.ldap.extras.controls.syncrepl_impl.SyncInfoValueFactory,org.apache.directory.api.ldap.extras.controls.syncrepl_impl.SyncRequestValueFactory,org.apache.directory.api.ldap.extras.controls.syncrepl_impl.SyncStateValueFactory
-Dapacheds.extendedOperations=org.apache.directory.api.ldap.extras.extended.ads_impl.cancel.CancelFactory,org.apache.directory.api.ldap.extras.extended.ads_impl.certGeneration.CertGenerationFactory,org.apache.directory.api.ldap.extras.extended.ads_impl.gracefulShutdown.GracefulShutdownFactory,org.apache.directory.api.ldap.extras.extended.ads_impl.storedProcedure.StoredProcedureFactory,org.apache.directory.api.ldap.extras.extended.ads_impl.gracefulDisconnect.GracefulDisconnectFactory
-Dlog4j.configuration=file:/usr/local/apacheds-2.0.0-M23/instances/default/conf/log4j.properties
-Dapacheds.log.dir=/usr/local/apacheds-2.0.0-M23/instances/default/log
-classpath /usr/local/apacheds-2.0.0-M23/lib/apacheds-service-2.0.0-M23.jar
org.apache.directory.server.UberjarMain
/usr/local/apacheds-2.0.0-M23/instances/default  

