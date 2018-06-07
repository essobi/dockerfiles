FROM rjeschmi/lmod  
  
MAINTAINER Robert Schmidt <rjeschmi@gmail.com>  
  
RUN useradd -u 1000 easybuild  
ADD build/config.cfg /software/config/config.cfg  
RUN chown -R easybuild.easybuild /software  
  
RUN mkdir -p /software/easybuild-develop  
RUN mkdir -p /software/easybuild/modules/all  
ADD build/install-EasyBuild-develop.sh /build/install-EasyBuild-develop.sh  
RUN chmod +x /build/install-EasyBuild-develop.sh  
  
RUN /build/install-EasyBuild-develop.sh hpcugent /software/easybuild-develop  
  
ADD build/z99_StdEnv.sh /etc/profile.d/z99_StdEnv.sh  
  
RUN mkdir -p /software/easybuild  
RUN chown -R easybuild.easybuild /software/easybuild  
  
RUN mkdir -p /export/easybuild  
RUN chown -R easybuild.easybuild /export  
  
ADD ./easybuild-docker.sh /usr/bin/easybuild-docker  
RUN chmod +x /usr/bin/easybuild-docker  
  
USER easybuild  
WORKDIR /export/easybuild  
  
VOLUME /export/easybuild  
VOLUME /software/easybuild-develop  
  
USER root  
RUN yum -y install python-keyring zlib-devel openssl-devel libibverbs-devel
unzip rpm-build python-setuptools  
  
USER easybuild  
  
CMD ["/usr/bin/easybuild-docker"]  
  

