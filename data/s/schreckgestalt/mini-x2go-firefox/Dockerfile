FROM debian:unstable-slim  
MAINTAINER Claude Henchoz "claude.henchoz@gmail.com"  
# Prerequisites  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install --no-install-recommends -y \  
openssh-server \  
gnupg2 \  
dirmngr \  
&& rm -rf /var/lib/apt/lists/*  
  
# X2Go install  
RUN apt-key adv --recv-keys --keyserver hkp://keys.gnupg.net:80
E1F958385BFE2B6E  
RUN echo 'deb http://packages.x2go.org/debian unstable main' | tee
/etc/apt/sources.list.d/x2go.list  
RUN apt-get update && apt-get install --no-install-recommends -y \  
x2goserver \  
x2goserver-xsession \  
pwgen \  
&& rm -rf /var/lib/apt/lists/*  
  
# SSH config  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config  
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g"
/etc/ssh/sshd_config  
  
# Desktop environment  
RUN apt-get update && apt-get install --no-install-recommends -y \  
xfce4 \  
xfce4-terminal \  
tango-icon-theme \  
firefox \  
&& rm -rf /var/lib/apt/lists/*  
  
# Finalization  
RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# Run  
EXPOSE 22  
CMD ["/run.sh"]  

