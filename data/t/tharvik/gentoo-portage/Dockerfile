FROM gentoo/stage3-amd64:latest  
  
RUN emerge-webrsync  
RUN eselect news read  
  
RUN echo 'EMERGE_DEFAULT_OPTS="--ask=n --jobs=2"' >> /etc/portage/make.conf  
RUN echo 'FEATURES="unknown-features-warn parallel-fetch parallel-install"' >>
/etc/portage/make.conf  
  
RUN mkdir /etc/portage/env  
RUN echo 'FEATURES="test"' > /etc/portage/env/test  
  
COPY emerge-accept /usr/bin/  

