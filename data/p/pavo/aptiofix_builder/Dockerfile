FROM centos  
LABEL maintainer="Pavo <brockbackups@gmail.com>"  
COPY setup.sh /root  
RUN yum -y group install "Development Tools" && \  
yum -y install epel-release acpica-tools libuuid-devel
https://www.nasm.us/pub/nasm/releasebuilds/2.13.03/linux/nasm-2.13.03-0.fc24.x86_64.rpm
&& \  
chmod +x /root/setup.sh  
ENTRYPOINT [ "./root/setup.sh" ]  

