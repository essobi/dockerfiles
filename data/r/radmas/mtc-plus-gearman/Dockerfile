# (!) Copy this file to your PHP project repository  
  
FROM radmas/mtc-plus-application  
  
MAINTAINER Fernando Moro <fernando.moro@radmas.com>  
  
LABEL org.mejoratuciudad.vendor="Radmas Technologies"  
LABEL org.mejoratuciudad.image-name="mtc-plus-application-code"  
LABEL description="Symfony2 Backoffice for Improve Your City."  
  
ARG version=1.0  
LABEL org.mejoratuciudad.version=${version}  
  
ARG env=mtc_dev  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#################################################  
# CODE  
  
ADD . /var/www/${env}  
  
RUN chown -R radmas:radmas /var/www/${env}  
  
#################################################  
# S6 OVERLAY  
  
USER root  
  
ENTRYPOINT ["/init"]  

