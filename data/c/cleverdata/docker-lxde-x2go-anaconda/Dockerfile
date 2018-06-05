FROM ubuntu:14.04.3  
MAINTAINER CleverDATA "support@cleverdata.ru"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && sudo apt-get upgrade -y \  
&& apt-get install -y openssh-server software-properties-common python-
software-properties \  
&& add-apt-repository ppa:x2go/stable \  
&& apt-get update -y \  
&& apt-get install -y x2goserver x2goserver-xsession x-window-system pwgen
libcurl3 libappindicator1 fonts-liberation  
&& apt-get install gconf-service libasound2 libgconf-2-4 libnspr4 libnss3
libpango1.0-0 libxss1 xdg-utils -y  
  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome*.deb \  
&& apt-get install -f \  
&& rm -rf google-chrome*.deb  
  
RUN ln -s /chrome.sh /usr/bin/chrome && ln -s /chrome.sh /usr/bin/chromium-
browser  
  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config && \  
sed -i "s/#PasswordAuthentication/PasswordAuthentication/g"
/etc/ssh/sshd_config && \  
sed -i "s/#X2GO_NXAGENT_DEFAULT_OPTIONS+=\" -clipboard
both\"/X2GO_NXAGENT_DEFAULT_OPTIONS+=\" -clipboard client\"/g"
/etc/x2go/x2goagent.options  
  
###ANACONDA INSTALL###  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-2.4.1-Linux-x86_64.sh
&& \  
/bin/bash /Anaconda2-2.4.1-Linux-x86_64.sh -b -p /opt/conda && \  
rm /Anaconda2-2.4.1-Linux-x86_64.sh  
  
  
###SET DESKTOP ENVIRONMENT###  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
ADD chrome.sh /chrome.sh  
RUN chmod +x /*.sh  
  
EXPOSE 22  
  
ENTRYPOINT ["/run.sh"]  
CMD ["-h"]

