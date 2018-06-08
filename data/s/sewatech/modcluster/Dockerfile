FROM sewatech/apache  
  
ADD proxy_cluster.load /etc/apache2/mods-available/  
ADD cluster.conf /etc/apache2/conf-available/  
  
RUN apt-get update && apt-get install -y curl && apt-get clean && \  
(curl -skL
http://downloads.jboss.org/mod_cluster/1.3.1.Final/linux-x86_64/mod_cluster-1.3.1.Final-
linux2-x64-so.tar.gz | tar xfz -) && \  
mv *.so /usr/lib/apache2/modules/ && \  
ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-enabled/ && \  
ln -s /etc/apache2/mods-available/proxy_ajp.load /etc/apache2/mods-enabled/ &&
\  
ln -s /etc/apache2/mods-available/proxy_cluster.load /etc/apache2/mods-
enabled/ && \  
ln -s /etc/apache2/conf-available/cluster.conf /etc/apache2/conf-enabled/  
  
ADD html/ /var/www/html/  

