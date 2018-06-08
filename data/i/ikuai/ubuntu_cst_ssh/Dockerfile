FROM ubuntu:16.04  
  
MAINTAINER Dylan <bbcheng@ikuai8.com>  
  
################################################################################  
# Locales  
ENV OS_LOCALE="en_US.UTF-8"  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y locales \  
&& locale-gen ${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LC_ALL=${OS_LOCALE} \  
LANGUAGE=en_US:en  
  
################################################################################  
# Allow ssh login, set timezone for china  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends --no-install-suggests openssh-
server tzdata \  
&& mkdir /var/run/sshd \  
&& ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
# RUN echo 'root:screencast' | chpasswd  
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  

