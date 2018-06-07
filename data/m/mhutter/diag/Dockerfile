FROM alpine:3.4  
MAINTAINER Manuel Hutter <manuel.hutter@vshn.ch>  
  
# this allows the container to be started as a service on PaaSes like
OpenShift  
CMD ["/bin/sleep", "1d"]  
  
RUN apk add --no-cache bind-tools curl  

