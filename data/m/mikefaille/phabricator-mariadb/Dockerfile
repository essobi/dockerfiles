FROM mariadb:10  
  
RUN mkdir -p /srv/www/phabricator/resources/sql/  
ADD
https://raw.githubusercontent.com/phacility/phabricator/master/resources/sql/stopwords.txt
/srv/www/phabricator/resources/sql/stopwords.txt  
RUN chmod 644 /srv/www/phabricator/resources/sql/stopwords.txt  
ADD etc/my.cnf.d /etc/mysql/conf.d  
  
# REPAIR TABLE phabricator_search.search_documentfield;  
# REPAIR TABLE phabricator_search.search_documentfield;  

