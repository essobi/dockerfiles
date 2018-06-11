#base os installation  
FROM ubuntu:wily  
  
MAINTAINER stephan Mgaya <smgayanath@gmail.com>  
  
#recomendation for auto installation oracle jdk  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
# Install the python script required for "add-apt-repository"  
RUN apt-get update && apt-get install -y software-properties-common  
  
# Sets language to UTF8 : this works in pretty much all cases  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# add new repo  
RUN add-apt-repository ppa:webupd8team/java  
  
# Install java //  
RUN apt-get update && apt-get install oracle-java7-installer -y  
  
# Setup JAVA_HOME, this is useful for docker commandline  
#ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
#RUN export JAVA_HOME  
RUN apt-get install zip wget -y  
  
#Download liferay with glassfish server 6.1 recomended  
RUN mkdir /opt/portal  
  
RUN cd /opt/portal/  
  
RUN wget
https://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.1.1%20GA2/liferay-
portal-glassfish-6.1.1-ce-ga2-20120731132656558.zip  
  
RUN unzip *.zip  
  
#clean space  
RUN rm -rf *.zip  
  
RUN chmod +x liferay-portal-6.1.1-ce-ga2/glassfish-3.1.2/bin/asadmin  
  
#set glassfish env export PATH=/opt/glassfish/bin:$PATH  
ENV PATH liferay-portal-6.1.1-ce-ga2/glassfish-3.1.2/bin:$PATH  
  
#Update glassfisg server password  
ADD run.sh /run.sh  
ADD change_admin_password.sh /change_admin_password.sh  
ADD change_admin_password_func.sh /change_admin_password_func.sh  
ADD enable_secure_admin.sh /enable_secure_admin.sh  
RUN chmod +x /*.sh  
  
#Adding grid engine  
#RUN cd /opt/portal/liferay-portal-6.1.1-ce-
ga2/glassfish-3.1.2/domains/domain1/lib/  
#RUN wget
http://grid.ct.infn.it/csgf/binaries/GridEngine/GridEngineDependencies.zip  
#downloading jsaga.  
RUN wget http://grid.ct.infn.it/csgf/binaries/GridEngine/jsaga-job-
management-1.5.11.jar  
  
RUN mv jsaga-job-management-1.5.11.jar /liferay-portal-6.1.1-ce-
ga2/glassfish-3.1.2/domains/domain1/lib/  
#ADMIN AND HTTP PORTS  
EXPOSE 8080 8181 4848  
#CMD["/run.sh"]  

