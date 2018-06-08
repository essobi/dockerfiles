FROM tutum/apache-php  
EXPOSE 80  
RUN apt-get update -y  
RUN apt-get install git-core -y  
RUN apt-get install curl -y  
RUN apt-get install mysql-client -y  
  
ADD ./scripts/install_drush.sh /scripts/install_drush.sh  
RUN /scripts/install_drush.sh  
  
ADD ./scripts/install_drupal.sh /scripts/install_drupal.sh  
RUN /scripts/install_drupal.sh  
  
ADD ./scripts/install_drupal_console.sh /scripts/install_drupal_console.sh  
RUN /scripts/install_drupal_console.sh  

