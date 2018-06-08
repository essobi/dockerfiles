FROM sergeyzh/centos6-java  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
RUN mkdir /home/jmeter ; cd /home/jmeter/ ; wget http://apache-
mirror.rbc.ru/pub/apache/jmeter/binaries/apache-jmeter-2.11.tgz ; \  
tar -xzf apache-jmeter-2.11.tgz ; rm apache-jmeter-2.11.tgz  
  
RUN yum install -y openssh-server ; sed -i '/#Port 22/ a \Port 2222'
/etc/ssh/sshd_config  
# Fix the problem with SSH login to container  
RUN sed -i "/pam_loginuid.so/ s/\\(.*\\)/#\1/" /etc/pam.d/sshd  
  
RUN /usr/sbin/adduser -p '$1$.m3inu2Y$1cgE5kmgCJ.wSdcScIAsk/' jmeter  
  
ADD run-services.sh /  
RUN chmod a+x /run-services.sh  
CMD /run-services.sh  
  
EXPOSE 2222  

