FROM tomcat:7  
  
RUN apt-get install -y unzip  
  
# Remove default webapps  
RUN rm -rf $CATALINA_HOME/webapps/*  
  
#  
# MOA-SP/SS  
#  
  
ADD bin $CATALINA_HOME/bin  
ADD wsdl /resources/wsdl  
  
RUN curl -O https://joinup.ec.europa.eu/system/files/project/b2/6b/e9/moa-
spss-1.5.1.tar.gz \  
&& tar xzf moa-spss-1.5.1.tar.gz \  
&& rm moa-spss-1.5.1.tar.gz \  
&& unzip moa-spss-1.5.1/moa-spss.war -x WEB-INF/lib/log4j*.jar -d webapps/moa-
spss \  
&& unzip -j moa-spss-1.5.1/moa-spss.war WEB-INF/lib/log4j*.jar -d lib \  
&& cp -r moa-spss-1.5.1/endorsed $CATALINA_HOME \  
&& cp -r moa-spss-1.5.1/ext/* $CATALINA_HOME/lib/ \  
&& mkdir $CATALINA_HOME/nativelibs \  
&& cp -r moa-spss-1.5.1/pkcs11/linux/* $CATALINA_HOME/nativelibs/ \  
&& mkdir -p conf/moa-spss \  
&& cp -r moa-spss-1.5.1/conf/moa-spss/certstore conf/moa-spss \  
&& cp -r moa-spss-1.5.1/conf/moa-spss/trustProfiles conf/moa-spss \  
&& cp moa-spss-1.5.1/conf/moa-spss/log4j.properties conf/moa-spss \  
&& cp moa-spss-1.5.1/conf/moa-spss/sp.minimum.config.xml conf/moa-spss \  
&& rm -rf moa-spss-1.5.1  
  
ENV MOA_SPSS_SERVER_CONFIGURATION $CATALINA_HOME/conf/moa-
spss/sp.minimum.config.xml  

