FROM getupcloud/cron-base-centos7  
  
MAINTAINER Diego Castro <diego.castro@getupcloud.com>  
  
ENV RUBY_VERSION=2.0  
  
LABEL io.k8s.description="Ruby 2.0 image for cron-based containers" \  
io.k8s.display-name="Cron 1.0 for Ruby 2.0" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,cron,cron1,ruby,ruby20"  
  
USER root  
  
RUN INSTALL_PKGS="ruby200 ruby200-ruby-devel ruby200-rubygem-rake v8314
ror40-rubygem-bundler nodejs010" && \  
EXTRA_INSTALL_PKGS="ImageMagick ImageMagick-devel rh-postgresql94-postgresql"
&& \  
yum install -y centos-release-scl && \  
yum install -y \--setopt=tsflags=nodocs $INSTALL_PKGS $EXTRA_INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS $EXTRA_INSTALL_PKGS && \  
yum clean all -y  
  
# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH  
COPY ./s2i/bin/ $STI_SCRIPTS_PATH  
# Each language image can have 'contrib' a directory with extra files needed
to  
# run and build the applications.  
COPY ./contrib/ /opt/app-root  
  
USER 1001  

