FROM ubuntu:latest  
  
MAINTAINER Igor Bronovskyi <admin@brun.if.ua>  
  
#========================  
# Miscellaneous packages  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
ca-certificates \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
#=================  
# Locale settings  
#=================  
ENV LANGUAGE uk_UA.UTF-8  
ENV LANG uk_UA.UTF-8  
RUN locale-gen uk_UA.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
language-pack-en \  
&& rm -rf /var/lib/apt/lists/*  
  
#===================  
# Timezone settings  
#===================  
ENV TZ "Europe/Kiev"  
RUN echo "Europe/Kiev" | sudo tee /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
RUN apt-get update  
RUN apt-get install -y vim mc w3m curl git  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
ADD ssh-welcome.sh /root/ssh-welcome.sh  
RUN chmod +x /root/ssh-welcome.sh && /root/ssh-welcome.sh  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  

