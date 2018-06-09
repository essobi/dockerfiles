# Use a specific version of the repository tools scripts  
# with the standard drush + composer base image.  
FROM uadrupal/base_drush_composer:1.0.1  
# Cherry-pick the scripts we actually want from the complete repo.  
RUN cd /tmp \  
&& git clone -b '1.4.1'
https://bitbucket.org/ua_drupal/uaqs_repository_tools.git \  
&& cp uaqs_repository_tools/reposync.sh /usr/local/bin/reposync \  
&& rm -Rf uaqs_repository_tools  

