FROM pulsepointinc/centos6-java8:latest  
  
COPY files/etc/yum.repos.d/cloudera-manager.repo /etc/yum.repos.d/  
  
RUN \  
rpm --rebuilddb && \  
yum install -y \  
cloudera-manager-agent \  
ntp && \  
yum clean all  
  
RUN \  
mkdir -p -v /usr/share/java && \  
curl -s -L -o /usr/share/java/mysql-connector-java.jar \  
"http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.39/mysql-
connector-java-5.1.39.jar"  
  
COPY files/activate.py /scripts/  
  
RUN \  
mkdir -p -v /opt/cloudera/parcel-cache && \  
curl -s -L -o /opt/cloudera/parcel-
cache/CDH-5.13.0-1.cdh5.13.0.p0.29-el6.parcel \  
"http://archive.cloudera.com/cdh5/parcels/5.13.0/CDH-5.13.0-1.cdh5.13.0.p0.29-el6.parcel"
&& \  
curl -s -L -o /opt/cloudera/parcel-cache/Anaconda-2.5.0-el6.parcel \  
"https://repo.continuum.io/pkgs/misc/parcels/archive/Anaconda-2.5.0-el6.parcel"
&& \  
curl -s -L -o /opt/cloudera/parcel-
cache/SPARK2-2.2.0.cloudera1-1.cdh5.12.0.p0.142354-el6.parcel \  
"http://archive.cloudera.com/spark2/parcels/2.2.0.cloudera1/SPARK2-2.2.0.cloudera1-1.cdh5.12.0.p0.142354-el6.parcel"
&& \  
/usr/lib64/cmf/agent/build/env/bin/python /scripts/activate.py && \  
rm -fr /opt/cloudera/parcel-cache/*  
  
COPY files/start.sh /scripts/  
  
CMD ["/scripts/start.sh"]  

