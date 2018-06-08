FROM busybox  
MAINTAINER Itxaka Serrano Garcia <itxakaserrano@gmail.com>  
  
RUN wget
"http://download.opensuse.org/repositories/systemsmanagement:/chef:/10/openSUSE_Leap_42.2/x86_64/ruby2.1-rubygem-
chef-10.32.2-19.5.x86_64.rpm" \--no-check-certificate -O /tmp/chef-client.rpm
&& \  
rpm2cpio /tmp/chef-client.rpm | cpio -idmv && \  
rm -rf /tmp/chef-client.rpm  
  
VOLUME [ "/opt/chef" ]  

