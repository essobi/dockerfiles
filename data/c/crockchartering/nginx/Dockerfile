# nginx-centos7  
# Here you can use whatever image base is relevant for your application.  
FROM centos:centos7  
  
# Here you can specify the maintainer for the image that you're building  
MAINTAINER Ricardo Katz <ricardo.katz@gmail.com>  
  
### Based on the Dockerfile and s2i scripts created by:  
#MAINTAINER Victor Palade <ipalade@redhat.com>  
# Source: https://github.com/openshift/source-to-
image/tree/master/examples/nginx-app  
# Set the labels that are used for Openshift to describe the builder image.  
LABEL io.k8s.description="Nginx Webserver" \  
io.k8s.display-name="Nginx 1.6.3" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,webserver,html,nginx" \  
# this label tells s2i where to find its mandatory scripts  
# (run, assemble, save-artifacts)  
io.openshift.s2i.scripts-url="image:///usr/libexec/s2i"  
# Install our Nginx package and clean the yum cache so that we don't have any  
# cached files waste space.  
RUN yum install -y epel-release && \  
yum install -y --setopt=tsflags=nodocs nginx && \  
yum clean all  
  
# We will change the default port for nginx (It's required if you plan on  
# running images as non-root user).  
# Also have to change the PID directory, as this have to be writable by root
group  
RUN sed -i 's/80/8080/' /etc/nginx/nginx.conf \  
&& sed -i 's/^pid.*/pid \/run\/nginx\/nginx.pid;/' /etc/nginx/nginx.conf  
  
# Sets the correct permission on nginx dynamic directories  
RUN mkdir -p /run/nginx && chmod -R 775 /run/nginx && chown -R 1001:0
/run/nginx \  
&& chown -R 1001:0 /var/log/nginx/ && chown -R 1001:0 /var/lib/nginx/  
  
# Copy the S2I scripts to /usr/libexec/s2i since we set the label that way  
COPY ["run", "assemble", "save-artifacts", "usage", "/usr/libexec/s2i/"]  
  
EXPOSE 8080  
# Sets a user so Origin can start this container  
USER 1001  
# Modify the usage script in your application dir to inform the user how to
run  
# this image.  
CMD ["/usr/libexec/s2i/usage"]  
  

