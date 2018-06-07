# Changing this may change the system Node.js/Python versions!  
# Under 18.04: Node.js is 8.10 and Python is 3.6.  
FROM ubuntu:18.04  
  
ARG APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN set -o errexit -o nounset \  
&& echo "Installing JDK, Node.js, Python" \  
&& apt-get update -yq \  
&& apt-get install -yq apt-utils \  
&& apt-get install -yq openjdk-8-jdk nodejs \  
&& apt-get install -yq python3 python3-pip python3-venv  
  
RUN set -o errexit -o nounset \  
&& echo "Installing Yarn, npm" \  
&& apt-get update -yq \  
&& apt-get install -yq curl gnupg npm \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update -yq \  
&& apt-get install -yq yarn \  
&& npm install npm@latest -g  
  
RUN set -o errexit -o nounset \  
&& echo "Installing geospatial libraries" \  
&& apt-get update -yq \  
&& apt-get install -yq binutils libproj-dev gdal-bin  
  
RUN set -o errexit -o nounset \  
&& echo "Installing command line tools" \  
&& apt-get update -yq \  
&& apt-get install -yq zip \  
&& pip3 install awscli requests  
  
RUN useradd -m bitbucket  
USER bitbucket  
WORKDIR /home/bitbucket  

