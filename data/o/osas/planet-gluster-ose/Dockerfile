FROM fedora:latest  
MAINTAINER Michael Scherer  
  
RUN dnf install -y make redhat-rpm-config git tar rubygem-bundler ruby-devel
curl-devel zlib-devel patch ImageMagick gcc-c++ findutils && dnf clean all  
RUN dnf install -y nginx && dnf clean all  
  
# we need -K 'UMASK=002' to make sure /srv/middleman is readable  
# -g 0 to have the right group  
# and fix the uid with -u for USER (need to be numeric)  
# all is in the doc  
# https://docs.openshift.org/latest/creating_images/guidelines.html#openshift-
origin-specific-guidelines  
RUN useradd middleman -d /srv/middleman -g 0 -K 'UMASK=002' -u 1000  
  
ADD . /srv/middleman  
WORKDIR /srv/middleman  
  
# gems need to be installed system wide,  
# for openshift online  
# since it use a different user on each run  
RUN /usr/bin/bundle install  
  
# make sure to report that to the kube config  
# maybe a wrapper would be better ?  
ENV PATH /usr/bin:/bin:/usr/local/bin  
  
RUN /usr/bin/bundle exec middleman build  
RUN /bin/cp /srv/middleman/deployment/nginx/nginx.conf /etc/nginx/nginx.conf  
RUN /usr/bin/chmod -R 770 /var/{lib,log}/nginx/ && chown -R :root
/var/{lib,log}/nginx/  
USER 1000  
CMD ["/usr/sbin/nginx"]  
  
EXPOSE 8080  

