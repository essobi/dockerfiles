FROM centos:6.6  
MAINTAINER Rodrigo Tsuru <caixapostal@gmail.com>  
RUN yum install -y curl \  
unzip \  
tar  
RUN cd /tmp && \  
curl -O -L
http://public.dhe.ibm.com/ibmdl/export/pub/software/products/en/MobileFirstPlatform/mobilefirst_studio_plugin_7.0.0.zip
&& \  
curl -O -L
http://eclipse.c3sl.ufpr.br/technology/epp/downloads/release/luna/SR2/eclipse-
jee-luna-SR2-linux-gtk-x86_64.tar.gz  
RUN cd /tmp && \  
tar xvzf eclipse-jee-luna-SR2-linux-gtk-x86_64.tar.gz && \  
rm eclipse-jee-luna-SR2-linux-gtk-x86_64.tar.gz  
RUN yum install -y java-1.7.0-openjdk-devel.x86_64  
RUN cd /tmp/eclipse && \  
./eclipse \  
-noSplash \  
-application org.eclipse.equinox.p2.director \  
-repository jar:file:///tmp/mobilefirst_studio_plugin_7.0.0.zip\\!/ \  
-followReferences \  
-installIUs com.ibm.imp.tools.wce.feature.feature.group,com.ibm.imp.dojo.tools.licensed.feature.feature.group,com.ibm.webtools.jquery.tools.licensed.feature.feature.group && \  
mv /tmp/eclipse /opt/eclipse && \  
rm /tmp/mobilefirst_studio_plugin_7.0.0.zip  
#RUN unzip
/opt/eclipse/plugins/com.worklight.studio.plugin_7.0.0.*/worklightServerInstance.zip
-d /opt/eclipse/plugins/com.worklight.worklight-
artifacts_7.0.0.*/liberty/wlp/usr/  
#RUN chmod +x /opt/eclipse/plugins/com.worklight.worklight-
artifacts_7.0.0.*/liberty/wlp/bin/server  
EXPOSE 10080  
CMD ["/opt/eclipse/eclipse"]  

