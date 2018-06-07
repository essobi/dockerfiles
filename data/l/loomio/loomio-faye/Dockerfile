FROM ruby:2.3.5  
COPY Gemfile.lock Gemfile private_pub.ru /loomio-faye/  
WORKDIR /loomio-faye  
RUN bundle install  
  
CMD thin --port 4443 \  
\--ssl \  
\--ssl-key-file $LOOMIO_SSL_KEY \  
\--ssl-cert-file $LOOMIO_SSL_CERT \  
\--ssl-disable-verify \  
\--environment production \  
\--rackup private_pub.ru \  
start  

