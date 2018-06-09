FROM centos:latest  
RUN yum-builddep -y java-1.8.0-openjdk  
RUN yum install -y java-1.8.0-openjdk-devel make file which unzip nano hg
compat-gcc-44 compat-gcc-44-c++ compat-glibc-headers-2.12 elfutils-libelf-
devel numactl-devel  
RUN useradd openjdk  
  
#Update git to latest, for OpenJ9  
RUN rpm -U http://opensource.wandisco.com/centos/7/git/x86_64/wandisco-git-
release-7-2.noarch.rpm && yum install -y git  
  
#Download freemarker for OpenJ9  
RUN cd /home/openjdk \  
&& curl -L
https://sourceforge.net/projects/freemarker/files/freemarker/2.3.8/freemarker-2.3.8.tar.gz/download
-o freemarker.tgz \  
&& tar -xvf freemarker.tgz freemarker-2.3.8/lib/freemarker.jar --strip=2 \  
&& chown openjdk:openjdk /home/openjdk/freemarker.jar \  
&& rm freemarker.tgz  
  
USER openjdk  
WORKDIR /home/openjdk  
  
ENTRYPOINT [ "/bin/bash" ]  

