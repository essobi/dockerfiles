FROM ruby:2.3  
RUN apt-get update -qq && apt-get install -y --no-install-recommends build-
essential  
  
# install postgres  
RUN apt-get install -y --no-install-recommends libpq-dev  
  
# install nokogiri  
RUN apt-get install -y --no-install-recommends libxml2-dev libxslt1-dev  
  
# install capybara-webkit  
RUN apt-get install -y --no-install-recommends libqt4-webkit libqt4-dev xvfb  
  
# install for a JS runtime  
RUN apt-get install -y --no-install-recommends nodejs  
  
# install imagemagick  
RUN apt-get install -y --no-install-recommends imagemagick  
  
# install libreoffice  
RUN apt-get install -y --no-install-recommends libreoffice  
  
# install FITS  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre  
  
ENV JAVA_VERSION 8u121  
ENV JAVA_DEBIAN_VERSION 8u121-b13-1~bpo8+1  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20161107~bpo8+1  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jre-headless="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
RUN mkdir /fits/  
RUN wget http://projects.iq.harvard.edu/files/fits/files/fits-1.0.2.zip -O
/fits/fits-1.0.2.zip  
RUN unzip /fits/fits-1.0.2.zip -d /fits  
RUN chmod a+x /fits/fits-1.0.2/fits.sh  
  
ENV PATH /fits/fits-1.0.2/:$PATH  
  
ENV APP_HOME /willow  
  
RUN mkdir $APP_HOME  
WORKDIR $APP_HOME  
  
ADD . $APP_HOME/  
RUN ls -al $APP_HOME  
RUN pwd  
  
ENV BUNDLE_GEMFILE=$APP_HOME/Gemfile \  
BUNDLE_JOBS=2 \  
BUNDLE_PATH=/bundle  
  
RUN bundle install  

