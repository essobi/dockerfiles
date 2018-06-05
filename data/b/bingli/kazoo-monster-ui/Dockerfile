FROM bingli/kazoo-base  
MAINTAINER Bing Li <bingli1000@gmail.com>  
  
RUN yum install -y httpd  
  
RUN yum -y --nogpgcheck localinstall http://repo.2600hz.com/Packages/Kazoo-
UI/CentOS_6/noarch/3.21/kazoo-ui-3.21-0.el6.noarch.rpm \  
http://repo.2600hz.com/Packages/Monster-UI-Core/CentOS_6/noarch/3.21/monster-
ui-core-3.21-4.el6.noarch.rpm \  
http://repo.2600hz.com/Packages/Monster-UI-Apps/CentOS_6/noarch/3.21/monster-
ui-accounts-3.21-2.el6.noarch.rpm \  
http://repo.2600hz.com/Packages/Monster-UI-Apps/CentOS_6/noarch/3.21/monster-
ui-numbers-3.21-1.el6.noarch.rpm \  
http://repo.2600hz.com/Packages/Monster-UI-Apps/CentOS_6/noarch/3.21/monster-
ui-pbxs-3.21-1.el6.noarch.rpm \  
http://repo.2600hz.com/Packages/Monster-UI-Apps/CentOS_6/noarch/3.21/monster-
ui-voip-3.21-2.el6.noarch.rpm \  
http://repo.2600hz.com/Packages/Monster-UI-Apps/CentOS_6/noarch/3.21/monster-
ui-webhooks-3.21-1.el6.noarch.rpm  
  
ADD entrypoint.sh /root/  
  
VOLUME ["/var/log"]  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  
EXPOSE 80  

