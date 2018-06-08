FROM garage/base  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
# Accepts oracle license  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections &&\  
/bin/echo debconf shared/accepted-oracle-license-v1-1 seen true |
/usr/bin/debconf-set-selections  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 &&\  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu $(/var/garage/base-
release) main" > /etc/apt/sources.list.d/webupd8team.list &&\  
apt-get update &&\  
/var/garage/install oracle-java7-installer &&\  
/var/garage/install oracle-java7-set-default default-jre  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/jre  
  
RUN /var/garage/install ant maven gradle  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# FROM $(ls /usr/lib/jvm/java-7-oracle/bin/* | xargs -n1 basename | tr "\n" "
")  
ENV GARAGE_PROVIDES appletviewer apt extcheck idlj jar jarsigner java java-
rmi.cgi javac javadoc javafxpackager javah javap javaws jcmd jconsole jcontrol
jdb jhat jinfo jmap jmc jps jrunscript jsadebugd jstack jstat jstatd jvisualvm
keytool native2ascii orbd pack200 policytool rmic rmid rmiregistry schemagen
serialver servertool tnameserv unpack200 wsgen wsimport xjc ant mvn gradle

