FROM holms/rvm-ree-rhel:latest  
MAINTAINER Roman Gorodeckij <it@swingcats.lt>  
  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN yum update -y \  
&& yum groupinstall -y 'Development Tools' \  
&& yum install -y libyaml-devel readline-devel zlib-devel openssl-devel
sqlite-devel pygpgme \  
&& yum groupremove -y "Development Tools" \  
&& curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-
binaries.phusionpassenger.com/yum/definitions/el-passenger.repo \  
&& yum-config-manager --enable cr \  
&& yum update -y \  
&& yum install -y passenger passenger-devel \  
&& yum remove -y libyaml-devel readline-devel zlib-devel openssl-devel sqlite-
devel \  
&& rm -rf /var/cache/yum/* \  
&& yum -y clean all  
  
  

