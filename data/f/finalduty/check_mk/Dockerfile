FROM finalduty/centos-base  
MAINTAINER "FinalDuty" <root@finalduty.me>  
EXPOSE 5000  
RUN yum install -y https://labs.consol.de/repo/stable/rhel7/x86_64/labs-
consol-stable.rhel7.noarch.rpm; #yum clean all -q -y  
RUN yum install -y omd; #yum clean all -q -y  
RUN yum install -y https://mathias-kettner.de/support/1.2.8p15/check-mk-
raw-1.2.8p15-el7-38.x86_64.rpm; #yum clean all -q -y  
RUN yum install -y https://mathias-kettner.de/support/1.2.8p21/check-mk-
raw-1.2.8p21-el7-44.x86_64.rpm; #yum clean all -q -y  
RUN yum install -y openssh-clients; yum update -y; #yum clean all -q -y  
  
RUN site='cmk'; \  
omd create $site \--no-init -u1000 -g1000; \  
omd config $site set APACHE_TCP_ADDR 0.0.0.0; \  
omd config $site set DEFAULT_GUI check_mk; \  
omd config $site set TMPFS off; \  
# omd start  
  
CMD omd update cmk; omd start; /bin/bash  

