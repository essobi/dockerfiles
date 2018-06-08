FROM outrigger/servicebase  
  
RUN yum -y update && \  
yum -y install varnish && \  
yum clean all  
  
EXPOSE 80  
ENV VARNISH_LISTEN_ADDRESS 0.0.0.0  
ENV VARNISH_LISTEN_PORT 80  
# Set the control terminal to be wide open by default, with no secret file.  
ENV VARNISH_ADMIN_LISTEN_ADDRESS 0.0.0.0  
ENV VARNISH_ADMIN_LISTEN_PORT 6082  
ENV VARNISH_STORAGE "malloc,64M"  
# A catch-all for any other options.  
ENV VARNISH_EXTRA_OPTS ""  
ENV VARNISH_BACKEND_HOST www  
ENV VARNISH_BACKEND_PORT 80  
ADD root /  

