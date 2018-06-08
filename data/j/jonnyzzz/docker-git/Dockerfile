FROM centos:6.6  
MAINTAINER Eugene Petrenko <Eugene.Petrenko@jetbrains.com>  
  
RUN \  
yum remove -y udev && \  
yum update -y && \  
yum groupinstall -y "Development tools" && \  
yum install -y tar wget m4 autoconf gcc \  
perl-ExtUtils-MakeMaker \  
curl-devel expat-devel \  
gettext-devel openssl-devel \  
zlib-devel && \  
yum clean all  
  
ENV GIT_VERSION 2.8.4  
ADD install_git.sh git.sh /root/  
  
RUN ["/bin/bash", "-c", "chmod a+x /root/install_git.sh && sync &&
/root/install_git.sh $GIT_VERSION && rm -rf /root/*git.sh"]  
  
CMD /bin/bash -c "cat /git; echo \"# Use the script to run git in container\""  
  

