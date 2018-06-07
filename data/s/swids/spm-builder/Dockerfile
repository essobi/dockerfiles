FROM swids/maven-test:debian  
  
ARG DS_VERSION=5.3  
ARG DS_FETCH_URL=http://updatesite.sierrawireless.com/developerStudio4/product  
RUN mkdir -p -m 777 /ds \  
&& wget ${DS_FETCH_URL}/devstudio-${DS_VERSION}-linux64.zip -O /ds/ds.zip \  
&& cd /ds \  
&& unzip -q ds.zip \  
&& rm ds.zip \  
&& cp legato-spm ant \  
&& sed -e
"s/com.swi.spm.headless.packagemanager/org.eclipse.ant.core.antRunner/g;s|-data
\$WORKDIR/wks|-data /tmp/wks|g" -i ant \  
&& mkdir -p /opt/tini \  
&& wget -O /opt/tini/tini
https://github.com/krallin/tini/releases/download/v0.16.1/tini \  
&& chmod 755 /opt/tini/tini  
  
ENTRYPOINT []  

