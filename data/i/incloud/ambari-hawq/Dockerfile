FROM incloud/ambari-agent  
  
#-----------install ambari-server (all in one)  
RUN yum clean all && yum -y install ambari-server  
  
#-------------local hawq rpm repo  
ADD PIVOTAL-HDB /opt/PIVOTAL-HDB/  
RUN cd /opt/PIVOTAL-HDB/ && cat hawq-2.0.0.0_beta-21030.x86_64.rpm.a* >
hawq-2.0.0.0_beta-21030.x86_64.rpm && rm -f
hawq-2.0.0.0_beta-21030.x86_64.rpm.a*  
COPY PIVOTAL-HDB/*.repo /etc/yum.repos.d/  
  
#-----------Bug fixes : rename hawq services script "constants.py ->
hawqconstants.py"  
COPY hawq/ambari/common-services/HAWQ/2.0.0/package/scripts/* /var/lib/ambari-
server/resources/common-services/HAWQ/2.0.0/package/scripts/  
#------------local HDP stack repo  
COPY hawq/ambari/repoinfo.xml /var/lib/ambari-
server/resources/stacks/HDP/2.3/repos/  
#------------install hawq service to HDP stack  
COPY hawq/ambari/services/HAWQ/* /var/lib/ambari-
server/resources/stacks/HDP/2.3/services/HAWQ/  
COPY hawq/ambari/services/PXF/* /var/lib/ambari-
server/resources/stacks/HDP/2.3/services/PXF/  
  
#-------------install hadoop_2.3 && hawq PXF && depends  
#COPY repo-local/* /etc/yum.repos.d/  
COPY repo-origin/* /etc/yum.repos.d/  
RUN yum clean all && yum -y install unzip hdp-select rpcbind 'hadoop_2_3_*'
snappy snappy-devel ntp hawq pxf-service apache-tomcat pxf-hdfs pxf-hive pxf-
hbase  
#RUN useradd pxf && useradd tomcat  
#/etc/pxf/conf/pxf-env.sh  
#------------------config for hawq & PXF  
RUN mkdir /usr/java && ln -s /opt/java/jdk1.8.0_60 /usr/java/default  
#user=gpadmin，passworkd=gpadmin（reference
-HAWQ\2.0.0.\package\scripts\common.py , __create_hawq_user() method）  
#RUN userdel -r gpadmin  
RUN useradd -p
'$6$04ecjJSX$fWelhVL1H1wJB0AR.OCcv.qthmhHVDLYvkZw8qW05kNFaoSFFEMDzjci2gniDN2ndCy3TBqOHoC91vK9eh.S/0'
gpadmin && su -c "ssh-keygen -q -f /home/gpadmin/.ssh/id_rsa -N ''" gpadmin &&
rm -f /home/gpadmin/.ssh/*  
  
#-------------install HUE && HUE service  
#RUN yum -y install wget tar asciidoc krb5-devel cyrus-sasl-gssapi cyrus-sasl-
devel libxml2-devel libxslt-devel libtidy mysql mysql-devel openldap-devel
python-devel python-simplejson python-setuptools sqlite-devel gcc gcc-c++
rsync saslwrapper-devel pycrypto gmp-devel libyaml-devel cyrus-sasl-plain
cyrus-sasl-devel cyrus-sasl-gssapi postgresql-devel python-psycopg2  
#COPY hue/hue-3.9.tgz /usr/local/  
#RUN wget -O /usr/local/hue-3.9.tgz
https://dl.dropboxusercontent.com/u/730827/hue/releases/3.9.0/hue-3.9.0.tgz  
#RUN cd /usr/local/ && tar -zxf hue-3.9.tgz && rm -rf hue-3.9.tgz && mv
hue-3.9.0 hue  
#COPY hue/HUE/ /var/lib/ambari-server/resources/stacks/HDP/2.3/services/HUE/  
COPY *.sh /  
RUN chmod +x /*.sh  
  
#clean yum cache  
RUN yum clean all  
  
VOLUME /var/lib/pgsql/data  
VOLUME /hadoop/hdfs/  
VOLUME /hadoop/zookeeper/  
VOLUME /data/hawq/  
  
WORKDIR /

