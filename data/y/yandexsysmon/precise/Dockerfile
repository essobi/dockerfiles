#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM ubuntu:14.04.1  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
ENV INITRD No  
  
# Work around initscripts trying to mess with /dev/shm:
<https://bugs.launchpad.net/launchpad/+bug/974584>  
# Used by our `src/ischroot` binary to behave in our custom way, to always say
we are in a chroot.  
ENV FAKE_CHROOT 1  
RUN mv /usr/bin/ischroot /usr/bin/ischroot.original  
ADD ischroot /usr/bin/ischroot  
  
# Configure no init scripts to run on package updates.  
ADD policy-rc.d /usr/sbin/policy-rc.d  
  
# Use source.list with all repositories and Yandex mirrors.  
ADD sources.list /etc/apt/sources.list  
RUN sed -i 's|://.*\\..*\\.com|://ru.archive.ubuntu.com|'
/etc/apt/sources.list  
  
RUN echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup  
RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache  
RUN echo 'Acquire::http {No-Cache=True;};' | tee /etc/apt/apt.conf.d/no-http-
cache  
  
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade
-y && apt-get clean  
  
# Install basic packages.  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
python-software-properties software-properties-common curl git htop unzip vim
wget build-essential tmux bash-completion && apt-get clean  
RUN chmod +s /usr/bin/sudo  
  
RUN rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*archive.ubuntu.com*  
  
# Add useful files.  
ADD root/.bashrc /root/.bashrc  
ADD root/.gitconfig /root/.gitconfig  
ADD root/scripts /root/scripts  
ADD root/.m2/settings.xml /root/.m2/settings.xml  
ADD env.sh /etc/profile.d/env.sh  
  
# Set working directory.  
ENV HOME /root  
ENV LC_ALL C.UTF-8  
WORKDIR /root  
  
ENTRYPOINT ["bash", "-c"]  
CMD ["bash"]  

