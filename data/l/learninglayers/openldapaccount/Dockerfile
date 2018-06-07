FROM learninglayers/tomcat:8.5.9  
MAINTAINER Yordan Manolov <manolov@dbis.rwth-aachen.de>  
  
RUN chmod 766 -R /opt  
  
#ADD account/ $TOMCAT_HOME/webapps # -> Device or resource busy  
ENV PWMCONF /opt/conf  
ENV PWMACC /opt/account  
  
ENV COPYACC cp -fR $PWMACC $TOMCAT_HOME/webapps  
ENV COPYCONF cp -fR $PWMCONF $TOMCAT_HOME/webapps  
ENV COPYCONFFILE cp $PWMCONF/PwmConfiguration.xml
$TOMCAT_HOME/webapps/account/WEB-INF  
  
ENTRYPOINT ["/bin/bash", "-c", "echo Copying account folder to
$TOMCAT_HOME/webapps && \  
$COPYACC && \  
echo Copying PwmConfiguration to $TOMCAT_HOME/webapps && \  
$COPYCONF && \  
sed -i s#LAYERS_API_URI#${LAYERS_API_URI}#g $PWMCONF/PwmConfiguration.xml \  
&& sed -i s#LDAP_ROOT_DN#${LDAP_ROOT_DN}#g $PWMCONF/PwmConfiguration.xml \  
&& sed -i s#LDAP_ROOT_USER#${LDAP_ROOT_USER}#g $PWMCONF/PwmConfiguration.xml \  
&& sed -i s#PWM_LDAP_ADMINS#${LAYERS_API_ADMIN}#g
$PWMCONF/PwmConfiguration.xml \  
&& sed -i s#TETHYS_IP#${TETHYS_IP}#g $PWMCONF/PwmConfiguration.xml \  
&& sed -i s#LDAP_PROXY_PASSWORD#${LDAP_PROXY_PASSWORD}#g
$PWMCONF/PwmConfiguration.xml \  
&& $COPYCONFFILE &&. /opt/init.sh"]  

