# Copyright (c) 2015, Mikkel Kroman <mk@maero.dk>  
#  
# Permission is hereby granted, free of charge, to any person obtaining  
# a copy of this software and associated documentation files (the  
# "Software"), to deal in the Software without restriction, including  
# without limitation the rights to use, copy, modify, merge, publish,  
# distribute, sublicense, and/or sell copies of the Software, and to  
# permit persons to whom the Software is furnished to do so, subject to  
# the following conditions:  
#  
# The above copyright notice and this permission notice shall be included  
# in all copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY  
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE  
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
FROM debian:latest  
MAINTAINER Mikkel Kroman <mk@maero.dk>  
  
# Create the journey user and group.  
RUN groupadd -r journey && useradd -r -g journey journey  
  
# Ensure that our package database is up to date.  
RUN apt-get update \  
&& apt-get install -y unzip curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Environment variables needed for download and verification of the package.  
ENV JOURNEY_VERSION 0.1.9  
ENV JOURNEY_DOWNLOAD_URL
"https://github.com/kabukky/journey/releases/download/v${JOURNEY_VERSION}/journey-
linux-amd64.zip"  
ENV JOURNEY_SHA256
"67d6280716a0e74d2daa03039d8544e6643b241d03f0e56da3cc23d21ab09b36"  
# Build and install Journey.  
RUN set -x \  
&& curl -sSL "${JOURNEY_DOWNLOAD_URL}" -o journey.zip \  
&& echo "${JOURNEY_SHA256} *journey.zip" | sha256sum -c - \  
&& unzip journey.zip && rm journey.zip \  
&& mkdir -p /srv/journey \  
&& mv journey-linux-amd64/* /srv/journey  
  
# Ensure that the /srv/journey directory is owned by the journey user.  
RUN chown -R journey:journey /srv/journey  
  
# Expose the required network ports.  
#  
# Port 8084 is the default HTTP port.  
# Port 8085 is the default HTTPS port.  
EXPOSE 8084 8085  
# Copy the entrypoint script and set it as our entry point.  
USER journey  
WORKDIR /srv/journey  
ENTRYPOINT ["/srv/journey/journey"]  

