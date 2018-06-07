FROM wking/gentoo-layman  
MAINTAINER Lucas Bickel <hairmare@purplehaze.ch>  
  
RUN layman -a betagarden  
RUN echo 'app-portage/layman-add ~amd64' >>
/etc/portage/package.accept_keywords/layman-add  
RUN emerge -v layman-add sudo  
RUN eselect news read new  

