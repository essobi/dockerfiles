# Rails on top of 'nepalez/ruby-passenger-nginx' with:  
#  
# * Ubuntu 14.04  
# * Git  
# * MRI Ruby 2.1.2  
# * Bundler  
# * Foreman  
# * Passenger  
# * Nginx  
#  
# Adds:  
#  
# * Autotests (guard-zeus, guard-rails)  
# * Code metrics (metric_fu, rubocop, brakeman, inch)  
# * Other useful packages for rails dev (annotate)  
#  
  
FROM nepalez/ruby-passenger-nginx  
MAINTAINER Andrew Kozin <andrew.kozin@gmail.com>  
  
# Update the system  
RUN apt-get update -qq  
  
# Add necessary gems globally  
RUN gem install \  
guard-zeus \  
guard-rails \  
metric_fu \  
rubocop \  
brakeman \  
inch \  
annotate  
  
# Expose Rails port  
EXPOSE 3000  
# Run a foreman by default  
CMD ["bundle", "exec", "foreman", "start"]  

