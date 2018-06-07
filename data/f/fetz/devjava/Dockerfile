FROM fetz/devcpp  
RUN \  
apt-get update && \  
apt-get install -y openjdk-8-jdk unzip && \  
dest="/opt" && \  
mkdir -p $dest && \  
curl -L
'https://eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/mars/2/eclipse-
jee-mars-2-linux-gtk-x86_64.tar.gz&r=1' | tar xzf - -C $dest && \  
curl -L http://www-us.apache.org/dist/tomcat/tomcat-8/v8.0.33/bin/apache-
tomcat-8.0.33.tar.gz | tar zxf - -C $dest && \  
curl -L http://www-us.apache.org/dist//db/derby/db-derby-10.12.1.1/db-
derby-10.12.1.1-bin.tar.gz | tar zxf - -C $dest && \  
curl -L
'http://www.eclipse.org/downloads/download.php?file=/rt/eclipselink/releases/2.6.2/eclipselink-2.6.2.v20151217-774c696.zip&r=1'
> $dest/eclipselink.zip && \  
cd $dest && unzip eclipselink.zip && rm eclipselink.zip && \  
chmod -R 777 $dest && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

