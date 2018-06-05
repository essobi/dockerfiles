FROM bibryam/base-jdk:latest  
MAINTAINER Bilgin Ibryam <bibryam@redhat.com>  
  
# EAP Version to use  
ENV EAP_VERSION jboss-eap-6.4  
# Add the EAP distribution to /opt  
ONBUILD ADD eap/ /opt/jboss  
ONBUILD RUN unzip -q -d $HOME/ $HOME/$EAP_VERSION.0.zip && rm
$HOME/$EAP_VERSION.0.zip  
  
ENV EAP_HOME /opt/jboss/$EAP_VERSION  
  
# The default port for deployed web applications.  
EXPOSE 8080  
# The Web Management Console port  
EXPOSE 9990  
# The port used by the Management Console and Management API  
EXPOSE 9999  
# This will boot EAP in the standalone mode and bind Public and Administration
interface to all network interface  
CMD ["./standalone.sh", "-b=0.0.0.0", "--server-config=standalone-full.xml",
"-bmanagement=0.0.0.0"]  

