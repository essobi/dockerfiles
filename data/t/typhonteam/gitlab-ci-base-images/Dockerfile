FROM ruby:2.3  
MAINTAINER Tech Typhon <tech@typhon.com>  
  
# Fix missing locales  
ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"  
# Skip interactive post-install scripts  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Don't install recommends  
RUN echo 'apt::install-recommends "false";' > /etc/apt/apt.conf.d/00recommends  
  
# Install ruby  
RUN apt-get update && apt-get install -y --force-yes \  
ruby-dev \  
ruby \  
make gcc build-essential \  
git  
  
# Install puppet 4.10  
RUN gem install puppet -v '~> 4.10.0'  
  
# Install puppet-lint and bundler  
RUN gem install bundler puppet-lint puppet-lint-absolute_classname-check
puppet-lint-classes_and_types_beginning_with_digits-check puppet-lint-
leading_zero-check puppet-lint-trailing_comma-check puppet-lint-
unquoted_string-check puppet-lint-variable_contains_upcase puppet-lint-
version_comparison-check puppet-lint-param-docs  
  

