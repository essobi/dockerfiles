FROM modera/php:5.6  
LABEL maintainer "Sergei Vizel <http://github.com/cravler>"  
  
ENV PHP_ALIAS PHP5  
  
ADD entrypoint.sh /entrypoint.sh  
  
RUN tail -n +2 /.cravler/entrypoint.sh >> /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

