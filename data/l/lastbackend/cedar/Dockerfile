FROM ubuntu-debootstrap:14.04  
COPY ./init.sh /tmp/build.sh  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive /tmp/build.sh  
  
ADD ./rootfs /  
  
RUN echo "install buildpacks"  
RUN curl
https://github.com/lastbackend/dockeruish/releases/download/v0.1.0/dockeruish_0.1.0_linux_x86_64.tgz
--silent -L | tar -xzC /bin  
RUN /bin/dockeruish buildpack install  
  
RUN ln -s /bin/dockeruish /build  
RUN ln -s /bin/dockeruish /start  
RUN ln -s /bin/dockeruish /exec  
  
CMD ["/bin/run"]  

