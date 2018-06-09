FROM stellartechnologies/docker-centos6-base:v1  
MAINTAINER Andy Kirkham <andy@spiders-lair.com>  
  
RUN yum -y update && yum clean all \  
&& yum -y install openssh-server xauth \  
&& yum -y install xorg-x11-fonts-misc \  
&& yum -y install xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-
Type1 \  
&& yum -y install libcanberra libcanberra-gtk2 \  
&& rpm -ivh http://javadl.sun.com/webapps/download/AutoDL?BundleId=106239 \  
&& useradd devel -d/home/devel && chmod 775 /home/devel && chown devel
/home/devel \  
&& cd /home/devel \  
&& wget http://eclipse.bluemix.net/packages/mars/data/eclipse-cpp-mars-R-
linux-gtk-x86_64.tar.gz \  
&& tar -zxf eclipse-cpp-mars-R-linux-gtk-x86_64.tar.gz \  
&& mv eclipse bin  

