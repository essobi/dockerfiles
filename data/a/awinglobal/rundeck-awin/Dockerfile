FROM jordan/rundeck:2.8.2  
  
RUN apt-get update && \  
apt-get install -y jq wget nginx && \  
wget
https://packages.chef.io/files/stable/chefdk/1.0.3/debian/7/chefdk_1.0.3-1_amd64.deb
-O chefdk.deb && \  
dpkg -i chefdk.deb && \  
rm -f chefdk.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD start.sh /  
ENTRYPOINT ["bash", "/start.sh"]  

