# Minimal Volt runtime image that can be used for production and/or  
# development. The image contains convenience scripts and extra stuff  
# to aid development and production deployment.  
#  
# For license information please see the accompanied LICENSE file in  
# this project.  
#  
# (C)Copyright Programlabbet AB 2015 (http://www.programlabbet.se)  
FROM programlabbet/mini-ruby:2.1.5-r1  
MAINTAINER Anders Hansson <anders@programlabbet.se>  
  
# Install the volt gem  
RUN gem install volt -v 0.9.6  
# RUN gem install thin  
RUN gem install puma  
  
# Install Node (used for precompiling)  
RUN apk --update add nodejs  
  
# Install additional useful packages used in production mode  
RUN apk --update add libjpeg-turbo-utils libjpeg  
  
# Make sure tmp folder exists  
RUN mkdir -p /tmp  
  
# Use tmp as our workdir when building/copying/unpacking binaries  
WORKDIR /tmp  
  
# Install pngcrush  
ADD files/pngcrush-1.7.88.tar.gz .  
WORKDIR /tmp/pngcrush-1.7.88  
RUN make && cp pngcrush /usr/bin/.  
  
# Install jpegoptim (not currently working as expected)  
#  
# ADD files/jpegoptim-1.4.3.tar.gz /tmp/  
# WORKDIR /tmp/jpegoptim-1.4.3  
# RUN ./configure && make && make install  
# Install jpeg-archive files  
ADD files/jpeg-archive-2.1.1-linux.tar.bz2 /usr/bin/  
  
# Install pngout  
WORKDIR /tmp  
ADD files/pngout-20150319-linux-static.tar.gz .  
RUN cp pngout-20150319-linux-static/x86_64/pngout-static /usr/bin/pngout  
  
# Restore workdir  
WORKDIR /  
  
# Remove temporary build files  
RUN rm -rf /tmp/*  
  
# Rebuild nginx under tmp  
RUN mkdir -p /tmp/nginx/client-body  
RUN chmod 777 -R /tmp/nginx  
  
# Install svgo  
RUN npm install -g svgo  
  
# Install image_optim packages (with binary package activated)  
#  
# FIXME: These are not currently working on Alpine as-is but require some  
# more investigation. We will automatically disable image compression  
# in the configuration file before we build the app to remove this  
# dependency.  
#  
# RUN gem install image_optim_pack  
# RUN gem install image_optim  
# Install Nginx  
RUN apk --update add nginx  
COPY nginx.conf /etc/nginx.conf  
COPY mime.types /etc/mime.types  
  
# Create paths for source (/src). Should be mapped to project root folder.  
RUN mkdir -p /src  
  
# Add some convenience scripts for starting/stopping/building the application.  
ADD scripts scripts/  
RUN chmod a+rx /scripts/*  
  
# Define the default ENTRYPOINT to start synchronizations and development mode  
#  
# By default this entrypoint will start in development mode as stated above,  
# although it *is* possible to start it in production mode.  
#  
# This entrypoint is *only* used if this image is not used as a base image for  
# a production build. It can be used to build a production app when starting  
# without defining a specific Dockerfile deriving from this image.  
#  
# It is however recommended that you do a complete prebuild and prepare of the  
# production Volt application in your derived Dockerfile and separate image  
# that is then deployed to your production server. Because any building  
# errors/problems would not show up until you actually do the build. Rather  
# handle those on the build server than on the production server.  
#  
# This option is provided to make it easier/quicker/faster to move forward to  
# a production state for non-critical applications that you may want to deploy  
# by simply doing a 'git pull' and then restart the container. YMMV!  
ENTRYPOINT sh -c '\  
/scripts/copy-src-to-app.sh;\  
if [ "$PRODUCTION_ENV" == "true" ]; then\  
/scripts/build-production-app.sh;\  
/scripts/start-prod.sh;\  
else\  
/scripts/start-dev.sh;\  
fi'  
  
# ============================================================================  
#  
# ONBUILD downstream build process  
#  
# Add ONBUILD steps to automatically build a production Volt application by  
# simply depending on this image.  
#  
# To create a production Volt image you just need to create a Dockerfile in  
# your root Volt app folder like this:  
#  
# echo >Dockerfile "FROM programlabbet/mini-volt"  
#  
# This will enable you to build a precompiled Volt application Docker image  
# with a 'docker build .' command.  
#  
# When run it should as default fire up your application in a container on  
# port 80. It does not contain a mongo database installation or anything else  
# so you need to make sure that the Volt container has access to the database  
# instance of your choice.  
#  
# If you need a simple mongo-db database setup for development purposes you  
# can use the Docker image programlabbet/mongodb-volt. But *PLEASE* beware!  
# There is absolutely NO SECURITY enabled and its only purpose is to provide  
# a quick-and-dirty way to get a development environment up and running for  
# your Volt application.  
# Setup some default build arguments  
ONBUILD ARG VOLT_PORT_WEBSOCKET=3000  
ONBUILD ARG VOLT_PORT_HTTP=80  
ONBUILD ARG VOLT_BASE_URL=""  
# ONBUILD ARG VOLT_ENV=production  
# Expose port 80 (for static files) and 3000 for websocket  
ONBUILD EXPOSE ${VOLT_PORT_HTTP:-80} ${VOLT_PORT_WEBSOCKET:-3000}  
  
# Add the application SOURCE code  
ONBUILD COPY . /app  
  
# Remove unecessary files and folders (like .git and caches)  
ONBUILD WORKDIR /app  
  
# Build production version of the application  
ONBUILD RUN sh -c '/scripts/build-production-app.sh'  
  
# Tweak the application for a specific base url  
# (Not activated for now)  
# ONBUILD RUN sh -c '/scripts/tweak_base_url.sh'  
# Add production entrypoint  
ONBUILD ENTRYPOINT sh -c '/scripts/start-prod.sh'  

