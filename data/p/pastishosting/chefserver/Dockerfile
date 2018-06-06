FROM quay.io/3ofcoins/chef-server  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https \  
&& apt-get purge -y chef chef-server-core \  
&& wget -qO - https://downloads.chef.io/packages-chef-io-public.key | apt-key
add \- \  
&& echo "deb https://packages.chef.io/stable-apt trusty main" >
/etc/apt/sources.list.d/chef-stable.list \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y chef-server-core chef \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD files/chef-server-setup.sh /chef-server-setup.sh  
RUN /bin/bash /chef-server-setup.sh  
  
ADD files/chef-server-startup.sh /chef-server-startup.sh  
CMD ["bash", "/chef-server-startup.sh"]  

