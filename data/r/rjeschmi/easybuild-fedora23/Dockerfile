FROM rjeschmi/lmod:fedora23-lmod6  
  
MAINTAINER Robert Schmidt <rjeschmi@gmail.com>  
  
RUN useradd -u 1000 build  
ADD build/config.cfg /software/config/config.cfg  
RUN chown -R build.build /software  
  
RUN mkdir -p /software/easybuild-develop  
ADD build/install-EasyBuild-develop.sh /build/install-EasyBuild-develop.sh  
RUN chmod +x /build/install-EasyBuild-develop.sh  
RUN /build/install-EasyBuild-develop.sh hpcugent /software/easybuild-develop  
  
ADD build/z99_StdEnv.sh /etc/profile.d/z99_StdEnv.sh  
  
RUN mkdir -p /software/easybuild  
RUN chown -R build.build /software/easybuild  
  
RUN mkdir -p /export/easybuild  
RUN chown -R build.build /export  
  
WORKDIR /export/easybuild  
VOLUME /export/easybuild  
VOLUME /software/easybuild-develop  
  
RUN dnf -y install python-setuptools python-keyring zlib-devel openssl-devel
libibverbs-devel unzip rpm-build  
  
USER build  
  
  

