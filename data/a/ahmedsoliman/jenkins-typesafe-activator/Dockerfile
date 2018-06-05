FROM ahmedsoliman/jenkins-slave:latest  
  
MAINTAINER Ahmed Soliman <me@ahmedsoliman.com>  
  
RUN wget "http://downloads.typesafe.com/typesafe-activator/1.2.10/typesafe-
activator-1.2.10-minimal.zip" && \  
unzip typesafe-activator-*.zip && \  
wget "https://dl.bintray.com/sbt/debian/sbt-0.13.6.deb" && \  
dpkg -i sbt-0.13.6.deb  
  
ENV PATH /data/activator-1.2.10-minimal:$PATH  
  
WORKDIR /data  
  
CMD ["./cmd.sh"]  

