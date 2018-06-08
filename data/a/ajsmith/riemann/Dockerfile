FROM fedora:25  
  
MAINTAINER Alex Smith <alex.smith@redhat.com>  
  
RUN groupadd -g 1001 riemann  
RUN useradd -r -d /var/lib/riemann -u 1001 -g 1001 -s /bin/false riemann  
RUN mkdir /var/lib/riemann && chown riemann:riemann /var/lib/riemann  
  
RUN dnf install -y
https://github.com/riemann/riemann/releases/download/0.2.12/riemann-0.2.12-1.noarch.rpm
&&\  
dnf clean all  
  
ADD riemann.config /etc/riemann/riemann.config  
  
EXPOSE 2003 5555 5556  
  
WORKDIR /var/lib/riemann  
USER riemann  
  
CMD ["/usr/bin/riemann"]  

