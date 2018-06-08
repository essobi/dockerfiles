FROM rodrigotsuru/ibmim-docker  
MAINTAINER Rodrigo Tsuru "caixapostal@gmail.com"  
RUN yum install -y curl  
COPY secure.dat /tmp/secure.dat  
COPY masterpw.txt /tmp/masterpw.txt  
COPY install.xml /tmp/install.xml  
RUN /opt/IBM/InstallationManager/eclipse/tools/imcl input /tmp/install.xml
-acceptLicense -showProgress -masterPasswordFile /tmp/masterpw.txt
-secureStorageFile /tmp/secure.dat  

