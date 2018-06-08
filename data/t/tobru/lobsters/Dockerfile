FROM ruby:2.5-alpine  
  
ARG GITHUB_NAMESPACE=lobsters/lobsters  
  
# Install static prerequisits  
RUN apk add --no-cache \  
wget \  
unzip \  
# dependencies for gems  
build-base \  
cmake \  
linux-headers \  
mariadb-dev \  
# dependencies for runtime  
nodejs \  
yarn  
  
# Define lobsters "version"  
# Note: There is no official release, so we stick to a Git hash  
# This is also used for build cache invalidation  
ENV LOBSTERS_HASH=33b333c \  
RAILS_ENV=openshift \  
HOME=/opt/lobsters  
  
# Install lobsters  
RUN mkdir /opt && cd /opt && \  
wget -q
https://github.com/"${GITHUB_NAMESPACE}"/archive/"${LOBSTERS_HASH}".zip
>/dev/null && \  
unzip "${LOBSTERS_HASH}".zip >/dev/null && rm "${LOBSTERS_HASH}".zip && \  
cd lobsters-* && cp -r . /opt/lobsters && cd /opt && rm -rf lobsters-* && \  
cd /opt/lobsters && \  
# Adding missing Gem  
echo "gem \"tzinfo-data\"" >> Gemfile && \  
# Install dependencies  
bundle install --without="test development"  
# Set working directoriy  
WORKDIR /opt/lobsters  
  
# Copy OpenShift / Docker specific files into image  
COPY bin/entrypoint /usr/local/bin/entrypoint  
COPY appcfg/database.yml /opt/lobsters/config/database.yml  
COPY appcfg/env_openshift.rb /opt/lobsters/config/environments/openshift.rb  
COPY appcfg/initializers_production.rb
/opt/lobsters/config/initializers/openshift.rb  
  
# OpenShift / Docker specific configuration  
RUN \  
# Configure secret_key_base via environment vars  
echo "Lobsters::Application.config.secret_key_base = ENV['SECRET_KEY_BASE']" \  
> /opt/lobsters/config/initializers/secret_token.rb  
  
# Filesystem permissions for OpenShift  
# https://docs.openshift.com/container-
platform/latest/creating_images/guidelines.html#openshift-specific-guidelines  
RUN chown -R 1001:0 /opt && \  
chmod -R g=u /opt && \  
chmod g=u /etc/passwd  
  
# Prepare runtime  
USER 1001  
EXPOSE 3000  
ENTRYPOINT [ "entrypoint" ]  
CMD ["rails", "server"]  

