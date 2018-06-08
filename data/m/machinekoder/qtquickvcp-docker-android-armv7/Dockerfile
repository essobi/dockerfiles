FROM library/debian:stretch  
MAINTAINER Alexander Rössler <mail@roessler.systems>  
RUN sed -i "s/httpredir.debian.org/ftp.us.debian.org/" /etc/apt/sources.list  
COPY init-install-packages.sh /tmp/init-install-packages.sh  
RUN /tmp/init-install-packages.sh  
COPY init-download-sdks.sh /tmp/init-download-sdks.sh  
RUN /tmp/init-download-sdks.sh  
COPY init-build-toolchain.sh /tmp/init-build-toolchain.sh  
RUN /tmp/init-build-toolchain.sh  

