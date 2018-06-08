FROM openjdk:7-jdk-alpine  
  
RUN mkdir /opt  
ADD files/semanticturkey-0.12.2+vb-bundle-2.4.4.zip /opt  
  
RUN cd /opt \  
&& unzip /opt/semanticturkey-0.12.2+vb-bundle-2.4.4.zip \  
&& rm -rf /opt/semanticturkey-0.12.2+vb-bundle-2.4.4.zip \  
&& ln -s /opt/semanticturkey-0.12.2-2017-03-02 semanticturkey  
  
# Configure data directory  
RUN dos2unix /opt/semanticturkey/etc/it.uniroma2.art.semanticturkey.cfg \  
&& sed -i
's/data.dir=..\/SemanticTurkeyData/data.dir=\/var\/local\/data\/SemanticTurkeyData/'
/opt/semanticturkey/etc/it.uniroma2.art.semanticturkey.cfg  
  
# Disable configuration file override during startup on clean installation  
RUN dos2unix /opt/semanticturkey/system/it/uniroma2/art/semanticturkey/st-
builder/0.12.2/st-builder-0.12.2-features.xml \  
&& sed -i 's/<configfile finalname="\/etc\/it.uniroma2.art.semanticturkey.cfg"
override="true">/<configfile
finalname="\/etc\/it.uniroma2.art.semanticturkey.cfg" override="false">/'
/opt/semanticturkey/system/it/uniroma2/art/semanticturkey/st-
builder/0.12.2/st-builder-0.12.2-features.xml  
  
VOLUME ["/var/local/data"]  
VOLUME ["/opt/semanticturkey/data/log"]  
  
CMD ["/opt/semanticturkey/bin/st_server_run", "server"]  

