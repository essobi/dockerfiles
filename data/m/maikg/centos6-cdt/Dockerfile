FROM maikg/centos6-wget  
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-
maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo  
RUN yum -y install gcc-c++ gcc make libusb1-devel java-1.8.0-openjdk
java-1.8.0-openjdk-devel apache-maven make rpm-build git  
CMD [ "/bin/bash", "--login" ]  

