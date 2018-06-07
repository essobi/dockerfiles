FROM base/archlinux  
  
RUN pacman --sync --refresh --sysupgrade --noconfirm --noprogressbar --quiet
&& pacman --sync --noconfirm --noprogressbar --quiet apache  
  
ADD httpd-ssl.conf /etc/httpd/conf/extra/httpd-ssl.conf  
ADD init.sh /init.sh  
  
RUN sed -i 's#\\#LoadModule ssl_module modules/mod_ssl.so#LoadModule
ssl_module modules/mod_ssl.so#' /etc/httpd/conf/httpd.conf  
RUN sed -i 's#\\#Include conf/extra/httpd-ssl.conf#Include conf/extra/httpd-
ssl.conf#' /etc/httpd/conf/httpd.conf  
  
CMD /init.sh  

