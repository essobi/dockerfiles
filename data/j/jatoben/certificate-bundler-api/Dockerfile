FROM ruby:2.4.0  
  
# Raise an error if Gemfile has been modified without bumping Gemfile.lock  
RUN bundle config \--global frozen 1  
  
ADD . /app  
WORKDIR /app  
  
RUN bundle install  
  
# OpenSSL::X509::DEFAULT_CERT_FILE defaults to /usr/lib/ssl/cert.pem,  
# which doesn't exist and causes the OpenSSL::X509::Store to throw exceptions.  
# Link the real cert bundle file into the right place to make the store happy  
RUN ln -s /usr/lib/ssl/certs/ca-certificates.crt /usr/lib/ssl/cert.pem  
  
RUN useradd -m app  
USER app  
  
CMD bundle exec puma -t ${MAX_THREADS:-5}:${MAX_THREADS:-5} -p ${PORT:-3000}
-e ${RACK_ENV:-development}  

