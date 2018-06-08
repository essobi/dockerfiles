FROM kujiy/kc-xoops:latest  
MAINTAINER kuji  
  
#RUN pear config-set http_proxy $http_proxy  
RUN pear channel-update pear.php.net  
RUN pear install -a Mail  
RUN pear install -a Mail_Mime  
RUN pear install --onlyreqdeps -f mail_mimedecode  
RUN pear install -a Log  
RUN pear install Image_Color2-alpha  
RUN pear install Image_Graph-alpha  
RUN pear install Auth  

