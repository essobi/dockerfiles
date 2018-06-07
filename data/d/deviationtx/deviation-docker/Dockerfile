FROM ubuntu:14.04  
MAINTAINER PhracturedBlue <deviationtx@gmail.com>  
RUN apt-get update && apt-get install -y build-essential git libc6-i386
mingw32 mingw32-binutils mingw32-runtime gettext zip python python-newt  
RUN cd /opt && curl --retry 10 --retry-max-time 120 -L
'https://launchpad.net/gcc-arm-embedded/4.8/4.8-2013-q4-major/+download/gcc-
arm-none-eabi-4_8-2013q4-20131204-linux.tar.bz2' | tar xfj -  
CMD ["/root/build_init.sh"]  
RUN mv /root /opt/root && ln -s /opt/root /root && chmod 755 /opt/root  
RUN ln -s /opt/docker /home/docker  
RUN echo "docker ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
COPY build.py /root/  
COPY build_init.sh /root/  
RUN sha1sum /root/build.py > /root/.build.py.sha1  
VOLUME /opt  
VOLUME /git  
VOLUME /release  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

