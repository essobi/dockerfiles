FROM opensuse:42.3  
ADD ansible /ansible/  
  
WORKDIR /ansible/  
  
RUN zypper --non-interactive in \--auto-agree-with-licenses python3
python3-PyYAML python-requests python3-requests ansible git which wget  
  
RUN ansible-playbook local.yml -c local  
  
ADD init.sh /ansible/  
RUN chmod +x init.sh  
  
ENV INVENTORY_GEN="repo" \  
HOSTS_REPO="https:\/\/your\/repo.git" \  
HOSTS_LIST="1 10 node domain" \  
HOSTS_URL="https:\/\/example.com\/munin_inventory" \  
APACHE_REQUIRE="all granted" \  
APACHE_DOMAIN="munin" \  
APACHE_MAIL="admin@munin"  
EXPOSE 80  
EXPOSE 4949  
VOLUME /etc/munin/  
VOLUME /etc/apache2/vhosts.d/  
VOLUME /var/lib/munin/  
  
ENTRYPOINT ["./init.sh"]  
CMD ["/usr/sbin/apachectl", "start", "-DFOREGROUND"]  

