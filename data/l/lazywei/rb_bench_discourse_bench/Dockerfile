FROM samsaffron/discourse_test  
  
MAINTAINER Bert Chang "https://github.com/lazywei"  
ADD rails_dispatcher.sh /var/www/discourse/rails_dispatcher.sh  
RUN chown discourse rails_dispatcher.sh  
RUN chmod u+x rails_dispatcher.sh  
  
ENTRYPOINT sudo -E -u discourse ./rails_dispatcher.sh  

