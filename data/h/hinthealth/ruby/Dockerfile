FROM ruby:2.4  
LABEL author="Gregory Hilkert <greg@hint.com>"  
  
# Install sentry cli  
RUN set -xe \  
curl -SL https://github.com/getsentry/sentry-
cli/releases/download/1.22.0/sentry-cli-Linux-x86_64 > sentry-cli \  
&& chmod 0755 sentry-cli \  
&& mv sentry-cli /usr/local/bin/sentry-cli  

