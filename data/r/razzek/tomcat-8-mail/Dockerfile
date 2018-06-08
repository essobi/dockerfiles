FROM razzek/tomcat-8  
  
RUN curl -SLfs
https://repo1.maven.org/maven2/com/sun/mail/javax.mail/1.5.6/javax.mail-1.5.6.jar
> $CATALINA_HOME/lib/javax.mail-1.5.6.jar \  
&& echo "5e6a70a6deed03bbbae6322af632b34c
$CATALINA_HOME/lib/javax.mail-1.5.6.jar" | md5sum -c \  
&& curl -SLfs
https://repo1.maven.org/maven2/javax/activation/activation/1.1/activation-1.1.jar
> $CATALINA_HOME/lib/activation-1.1.jar \  
&& echo "8ae38e87cd4f86059c0294a8fe3e0b18
$CATALINA_HOME/lib/activation-1.1.jar" | md5sum -c  

