FROM centos:7  
RUN yum install -y wget java-1.7.0-openjdk tar  
RUN wget -O mint.tar.gz
"http://dev.redboxresearchdata.com.au/nexus/service/local/artifact/maven/redirect?r=snapshots&g=com.googlecode.redbox-
mint&a=mint-distro&v=LATEST&c=build&e=tar.gz"; tar xvfz mint.tar.gz -C /opt/;
rm /mint.tar.gz;chmod +x /opt/mint/server/tf_fg.sh  
CMD /opt/mint/server/tf_fg.sh  

