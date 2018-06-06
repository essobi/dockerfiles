FROM rapi/rapidapp:1.3100  
MAINTAINER Henry Van Styn <vanstyn@cpan.org>  
  
# This is manually updated when new tags are created  
ENV RAPI_PSGI_IMAGE_VERSION=1.3100  
# Install some misc useful Plack packages:  
RUN cpanm \  
Plack::Middleware::Headers \  
Plack::Middleware::TemplateToolkit \  
Log::Dispatch::FileRotate \  
&& rm -rf .cpanm/  
  
# Install Rapi::Blog 1.0101  
RUN cpanm http://www.cpan.org/authors/id/V/VA/VANSTYN/Rapi-Blog-1.0101.tar.gz
&& rm -rf .cpanm/  
  
RUN mkdir -p /opt/app \  
&& mkdir -p /opt/misc  
  
VOLUME /opt/app  
WORKDIR /opt/app  
  
# No longer expose ports by default  
# -- expect use '-p' or EXPOSE in downstream images  
#EXPOSE 3000 3500 5000  
# env flag used by CMD script to prevent running except from here  
ENV RAPI_PSGI_DOCKERIZED 1  
# Alias/symlink to allow calling different commands using docker run/exec ...  
# we are creating the symlinks before copying the actual file to avoid  
# the need to re-run this step after a simple change to the script  
RUN ln -sf /rapi_psgi_control.pl /bin/via-git \  
&& ln -sf /rapi_psgi_control.pl /bin/init-stopped \  
&& ln -sf /rapi_psgi_control.pl /bin/app-restart \  
&& ln -sf /rapi_psgi_control.pl /bin/stop-app \  
&& ln -sf /rapi-install-extras.sh /bin/rapi-install-extras  
  
# This is how we would install extras to the image (and is also  
# how downstream images should install them, if desired):  
#RUN rapi-install-extras  
# This will exec rapi_psgi_control.pl when there are no arguments:  
ENTRYPOINT ["/entrypoint.pl"]  
  
# We're doing this last for faster rebuilds when only changing the scripts  
COPY rapi_psgi_control.pl /  
COPY entrypoint.pl /  
COPY rapi-install-extras.sh /  
COPY bashrc /root/.bashrc  
  
# Make sure the scripts are executable  
RUN chmod ugo+x /*.pl /*.sh  

