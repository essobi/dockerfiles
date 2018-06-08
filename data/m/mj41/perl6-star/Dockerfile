FROM fedora:25  
MAINTAINER Michal Jurosz <docker@mj41.cz>  
  
RUN dnf install -y perl make gcc tar git findutils which \  
perl-autodie perl-Test-Harness perl-ExtUtils-Command \  
perl-devel perl-Filter-Simple perl-ExtUtils-Embed perl-Test-Simple \  
&& dnf clean all  
  
RUN useradd urak  
WORKDIR /home/urak/  
  
COPY cache/* /home/urak/cache/  
RUN chmod -R a+rw /home/urak/cache/  
  
USER urak  
ENV HOME /home/urak  
RUN mkdir -p /home/urak/rakudo-install/  
COPY dockerfile-bin/base.sh /home/urak/dockerfile-bin/  
RUN /home/urak/dockerfile-bin/base.sh release 2016.11 /home/urak/rakudo-
install  
  
ENV PATH $PATH:/home/urak/rakudo-install/bin:/home/urak/rakudo-
install/share/perl6/site/bin  
  
COPY dockerfile-bin/extra-modules.sh /home/urak/dockerfile-bin/  
RUN /home/urak/dockerfile-bin/extra-modules.sh  
  
USER root  
RUN rm -rf /tmp/* /var/tmp/* /home/urak/dockerfile-bin /home/urak/cache  
  
USER urak  
RUN perl6 -e'say "{$*PERL.compiler.gist} on {$*VM.gist} for {$*DISTRO.gist}"'  
CMD /bin/bash  

