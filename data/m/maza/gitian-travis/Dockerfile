FROM ubuntu:15.10  
RUN apt-get update \  
&& apt-get install -y python python-pip wget git apache2 ruby qemu-utils apt-
cacher-ng lxc sudo debootstrap net-tools  
RUN mkdir /gitian \  
&& cd /gitian \  
&& wget http://archive.ubuntu.com/ubuntu/pool/universe/v/vm-builder/vm-
builder_0.12.4+bzr489.orig.tar.gz \  
&& echo "ec12e0070a007989561bfee5862c89a32c301992dd2771c4d5078ef1b3014f03 vm-
builder_0.12.4+bzr489.orig.tar.gz" | sha256sum -c \  
&& tar -zxvf vm-builder_0.12.4+bzr489.orig.tar.gz \  
&& cd vm-builder-0.12.4+bzr489 \  
&& python setup.py install \  
&& cd .. \  
  
RUN cd /gitian ; git clone https://github.com/devrandom/gitian-builder.git  
  
RUN cd /gitian \  
&& echo "lxc.aa_allow_incomplete = 1" >> gitian-builder/etc/lxc.config.in \  
&& echo "lxc.aa_profile = unconfined" >> gitian-builder/etc/lxc.config.in  
  
RUN adduser --disabled-password --gecos "gitian" \--uid 1001 gitian  
  
ADD . /  
  
RUN mv /gitian_build.sh /gitian/  
RUN mv /make_gitian_vms.sh /gitian/  
RUN mv /config-lxc /gitian/gitian-builder/libexec/  
RUN mv /travis_wait.sh /gitian/gitian-builder/  
  
RUN chmod +x /gitian/gitian_build.sh /gitian/gitian-builder/travis_wait.sh
/gitian/gitian-builder/libexec/config-lxc /gitian/make_gitian_vms.sh \  
&& chown -R gitian /gitian  
  
RUN echo "gitian ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/gitian  
  
ENV LXC=1  
ENV USE_LXC=1  
ENV GITIAN_HOST_IP=10.0.3.1  
ENV LXC_GUEST_IP=10.0.3.5  
ENV MIRROR_HOST=127.0.0.1  
USER gitian  
WORKDIR ["/gitian"]  
ENTRYPOINT ["/gitian/make_gitian_vms.sh"]  

