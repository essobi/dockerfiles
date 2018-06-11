FROM sergeyzh/centos6-nginx:latest  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
RUN yum install --enablerepo=extras -y epel-release centos-release-SCL \  
&& rpm -i https://repo.wallarm.com/centos/wallarm-
node/6/x86_64/Packages/wallarm-node-repo-1-2.el6.noarch.rpm \  
&& yum install -y wallarm-node cronie  
  
RUN sed -i 's|/etc/nginx/||g' /etc/nginx/nginx.conf  
  
ADD functions.sh /  
ADD run-services.sh /  
RUN chmod +x /run-services.sh ; mkdir -p /conf/nginx  
  
CMD /run-services.sh

