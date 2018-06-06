FROM bitnami/moodle:3.2.2-r3  
  
# Remove original wwwroot lines  
RUN sed -i -e '/HTTPS/,+4d' /opt/bitnami/moodle/config.php  
# Make all links to go through SSL  
RUN sed -i "$(grep -n dataroot config.php | cut -f1 -d:)i \$CFG->wwwroot =
'https://' . $_SERVER['HTTP_HOST'];" /opt/bitnami/moodle/config.php  
# Tell Moodle we're using an SSL proxy where the SSL is terminated before
reaching Moodle  
RUN sed -i "$(grep -n wwwroot config.php | cut -f1 -d:)i \$CFG->sslproxy = 1"
/opt/bitnami/moodle/config.php  

