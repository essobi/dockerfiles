#*******************************************************************************  
# Copyright 2015 Hewlett Packard Enterprise Development Company, L.P.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and
limitations under the License.  
#*******************************************************************************  
# Verigreen Collector Dockerfile  
# ==============================  
# ## Purpose  
# - Builds an image for the Verigreen Collector App  
# ## Maintainer(s):  
# - Ricardo Quintana https://github.com/rqc  
#  
FROM tomcat:7.0.57-jre7  
MAINTAINER Ricardo Quintana https://github.com/rqc  
  
# Install necessary OS packages, including:  
# - `Git`  
# - `host` - for automated deployment scripts  
RUN apt-get update && apt-get install -y \  
\--fix-missing \  
curl \  
git \  
tar \  
bash \  
host \  
gawk \  
apt-utils \  
locales-all \  
locales \  
&& \  
apt-get clean  
  
# Install locales  
#RUN apt-get install -y apt-utils  
#RUN apt-get install -y locales-all locales  
# Set UTF-8 English Locale  
RUN locale-gen en_US en_US.UTF-8  
RUN dpkg-reconfigure locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Environment variables that point to directories.  
ENV VERIGREEN_RELEASE="verigreen-2.5.6"  
ENV APP_DIR="/app" \  
VG_HOME="/vg" \  
VG_REPO="/repo" \  
VG_SSH="/ssh" \  
ROOT_SSH_DIR="/root/.ssh" \  
TOMCAT_WEBAPPS_DIR="/usr/local/tomcat/webapps" \  
VG_DOWNLOAD_URL="https://github.com/Verigreen/verigreen/releases/download/$VERIGREEN_RELEASE/verigreen-
collector.war"  
# Create directories for Verigreen  
# Download the release source code for verigreen (from Github)  
# Build the entire Verigreen project and copy war to tomcat webapps directory.  
# Finally, cleanup and prepare startup scripts.  
RUN mkdir -p $VG_HOME && \  
mkdir -p $APP_DIR && \  
mkdir -p $VG_SSH && \  
mkdir -p $ROOT_SSH_DIR && \  
rm -rf $TOMCAT_WEBAPPS_DIR/ROOT && \  
curl -SL "$VG_DOWNLOAD_URL" -o "$TOMCAT_WEBAPPS_DIR/ROOT.war"  
  
# Add the `docker-entrypoint.sh` script which will setup correctly the
container's environment for Verigreen and it will start the app.  
ADD docker-entrypoint.sh $APP_DIR/  
  
# Change to the root directory where our scripts will be located.  
WORKDIR $APP_DIR  
  
# Prepare script for execution.  
RUN chmod +x docker-entrypoint.sh  
  
# add a tomcat setenv.sh file with VG_HOME parameter  
RUN echo "export CATALINA_OPTS=\"-Denv.VG_HOME=/vg\"" >
/usr/local/tomcat/bin/setenv.sh  
  
# Run Verigreen using deployment script `docker-entrypoint.sh`.  
# Default Verigreen port is `8080` and is exposed by parent tomcat image.  
CMD ["./docker-entrypoint.sh"]

