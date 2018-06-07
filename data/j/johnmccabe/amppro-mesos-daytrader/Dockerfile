FROM gliderlabs/alpine:3.3  
RUN apk-install openjdk8-jre-base ; \  
apk-install bash ; \  
apk-install curl  
  
ENV AMP_PRO_VERSION 3.1.0-20160327.1622  
ENV brooklyn.webconsole.security.users docker  
ENV brooklyn.webconsole.security.user.docker.password docker  
  
RUN curl -O -s -S http://developers.cloudsoftcorp.com/amp-pro/amp-pro-
dist-${AMP_PRO_VERSION}-dist.tar.gz ; \  
tar zxf amp-pro-dist-${AMP_PRO_VERSION}-dist.tar.gz ; \  
rm -f amp-pro-dist-${AMP_PRO_VERSION}-dist.tar.gz; \  
mkdir /root/.brooklyn; \  
echo "brooklyn.experimental.feature.tosca = false" >
/root/.brooklyn/brooklyn.properties; \  
chmod 600 /root/.brooklyn/brooklyn.properties  
  
WORKDIR /cloudsoft-amp-pro-${AMP_PRO_VERSION}  
  
VOLUME [ "/root/.brooklyn", "/root/.ssh" , "/root/.brooklyn-persistence" ]  
  
EXPOSE 8081  
ENTRYPOINT /cloudsoft-amp-pro-${AMP_PRO_VERSION}/bin/amp launch --persist auto
--persistenceDir /root/.brooklyn-persistence --catalogAdd
https://s3.amazonaws.com/amp-daytrader-mesos-
demo/tmp_dir_pending_public_repos/mesos.bom,https://s3.amazonaws.com/amp-
daytrader-mesos-demo/tmp_dir_pending_public_repos/websphere-
liberty.bom,https://s3.amazonaws.com/amp-daytrader-mesos-
demo/tmp_dir_pending_public_repos/wildfly10.bom,https://s3.amazonaws.com/amp-
daytrader-mesos-demo/tmp_dir_pending_public_repos/daytrader-websphereliberty-
cluster.bom,https://s3.amazonaws.com/amp-daytrader-mesos-
demo/tmp_dir_pending_public_repos/daytrader-wildfly-cluster.bom  
  

