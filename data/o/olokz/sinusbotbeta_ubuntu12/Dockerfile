FROM ubuntu:12.04  
MAINTAINER Olokz "https://github.com/Olokz"  
ENV ROOT_PASS="@hyujG667$r"  
RUN apt-get update  
RUN apt-get install -y x11vnc xinit xvfb libxcursor1 ca-certificates bzip2
curl libglib2.0-0 nano sudo screen  
RUN apt-get install -y libxml-parser-perl libpath-class-perl perl-modules
screen pure-ftpd rsync sudo e2fsprogs subversion unzip  
RUN apt-get install -y libarchive-zip-perl  
RUN apt-get install -y ia32-libs  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo root:"$ROOT_PASS" | chpasswd  
  
RUN chage -d 0 root  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
EXPOSE 8087  
CMD ["/usr/sbin/sshd", "-D"]  

