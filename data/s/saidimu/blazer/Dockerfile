FROM rails:onbuild  
RUN set -x; \  
rails g blazer:install --skip && \  
rake db:migrate  
  
## for mounting the db files on the host or in another volume  
VOLUME /usr/src/app/db  

