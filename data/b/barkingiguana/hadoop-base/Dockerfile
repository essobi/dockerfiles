FROM barkingiguana/java  
  
MAINTAINER Craig R Webster <craig@barkingiguana.com>  
  
ADD cdh4.list /etc/apt/sources.list.d/cdh4.list  
ADD cdh4.key /tmp/cdh4.key  
RUN DEBIAN_FRONTEND=noninteractive apt-key add /tmp/cdh4.key && rm
/tmp/cdh4.key  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update  
ADD conf /etc/hadoop/conf.barkingiguana  
RUN update-alternatives --install /etc/hadoop/conf hadoop-conf
/etc/hadoop/conf.barkingiguana 50  
RUN update-alternatives --set hadoop-conf /etc/hadoop/conf.barkingiguana  

