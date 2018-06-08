# heavily based upon  
# - https://registry.hub.docker.com/u/centurylink/ruby-base/  
# - https://registry.hub.docker.com/u/atlashealth/ruby  
FROM debian:8.1  
  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
# NOTES:  
# - git is here for private gem dependencies in Gemfiles  
# - ssh is also used by private gem dependencies in Gemfiles  
ENV RUBY_BUILD_DEPENDENCIES curl build-essential libffi-dev libgdbm-dev
libreadline6-dev  
ENV COMMON_GEM_DEPENDENCIES ca-certificates libcurl4-gnutls-dev libssl-dev
libxml2 \  
libyaml-dev git ssh  
  
ENV RUBY_MAJOR 2.2  
ENV RUBY_VERSION 2.2.3  
ENV RUBY_SHA256
df795f2f99860745a416092a4004b016ccf77e8b82dec956b120f18bdc71edce  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -y -q \  
$RUBY_BUILD_DEPENDENCIES $COMMON_GEM_DEPENDENCIES \  
# Install ruby  
&& mkdir -p /tmp/ruby \  
&& curl -s -o /tmp/ruby-$RUBY_VERSION.tar.gz http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz \  
&& echo "${RUBY_SHA256} /tmp/ruby-$RUBY_VERSION.tar.gz" >
/tmp/ruby-$RUBY_VERSION.sha256 \  
&& sha256sum -c /tmp/ruby-$RUBY_VERSION.sha256 \  
&& tar --strip-components=1 -C /tmp/ruby -zxf /tmp/ruby-$RUBY_VERSION.tar.gz \  
&& cd /tmp/ruby \  
&& ./configure --disable-install-doc \  
&& make \  
&& make install \  
# Clean and uninstall components that aren't needed  
&& rm -r /tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get remove -y $RUBY_BUILD_DEPENDENCIES \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& truncate -s 0 /var/log/*log  
  
# Don't install rdoc and ri files for any gem  
RUN echo 'gem: --no-document --no-rdoc --no-ri' > /etc/gemrc  
  
RUN gem update --system \  
&& gem install bundler  
  
CMD [ "irb" ]  
  

