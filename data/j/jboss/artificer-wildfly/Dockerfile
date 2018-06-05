FROM jboss/wildfly:8.2.0.Final  
  
MAINTAINER Brett Meyer <brmeyer@redhat.com>  
  
ENV ARTIFICER_VERSION 1.0.0.Final  
  
RUN cd $HOME \  
&& curl http://downloads.jboss.org/artificer/artificer-$ARTIFICER_VERSION.zip
| bsdtar -xvf- \  
&& cd artificer-$ARTIFICER_VERSION \  
&& chmod 777 install.sh \  
&& ./install.sh -Ds-ramp-distro.choices.platform=1 -Ds-ramp-
distro.choices.platform.jboss-wildfly-8.path=$HOME/wildfly -Dejb-
jms.password=artificer1! \  
&& cp artificer-realm.json $HOME/wildfly \  
&& cd .. \  
&& rm -rf artificer*  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-c",
"standalone-full.xml", "-Dkeycloak.import=wildfly/artificer-realm.json",
"-Dhibernate.hbm2ddl.auto=update"]  

