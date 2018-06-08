# bash-4.3# ldd /bin/consul  
# /lib64/ld-linux-x86-64.so.2 (0x7f806af08000)  
# libpthread.so.0 => /lib64/ld-linux-x86-64.so.2 (0x7f806af08000)  
# libc.so.6 => /lib64/ld-linux-x86-64.so.2 (0x7f806af08000)  
# Error relocating /bin/consul: __fprintf_chk: symbol not found  
# Error relocating /bin/consul: __sprintf_chk: symbol not found  
#  
# See  
# http://www.blang.io/2015/04/19/golang-alpine-build-golang-binaries-for-
alpine-linux.html  
# http://www.openwall.com/lists/musl/2015/06/17/1  
FROM debian:jessie  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y bash curl unzip && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ADD https://dl.bintray.com/mitchellh/consul/0.5.2_linux_amd64.zip
/tmp/consul.zip  
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm
/tmp/consul.zip  
  
ADD https://dl.bintray.com/mitchellh/consul/0.5.2_web_ui.zip /tmp/webui.zip  
RUN cd /tmp && unzip /tmp/webui.zip && mv dist /ui && rm /tmp/webui.zip  
  
ADD https://get.docker.io/builds/Linux/x86_64/docker-1.7.0 /bin/docker  
RUN chmod +x /bin/docker  
  
ADD ./config /config/  
ONBUILD ADD ./config /config/  
  
ADD ./start /bin/start  
ADD ./check-http /bin/check-http  
ADD ./check-cmd /bin/check-cmd  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp  
VOLUME ["/data"]  
  
ENV SHELL /bin/bash  
  
ENTRYPOINT ["/bin/start"]  
CMD []  

