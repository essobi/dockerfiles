FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Configure timezone and locale to spanish and America/Bogota timezone. Change
locale and timezone to whatever you want  
ENV LANG="fr_FR.UTF-8"  
ENV LANGUAGE=fr_FR  
RUN locale-gen fr_FR.UTF-8 && locale-gen fr_FR  
RUN echo "Europe/Paris" > /etc/timezone && \  
apt-get install -y locales && \  
sed -i -e "s/# $LANG.*/$LANG.UTF-8 UTF-8/" /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=$LANG  
  
RUN apt-get update && apt-get install -y vim xterm pulseaudio cups curl  
# Goto https://www.nomachine.com/download/download&id=10 and change for the
latest NOMACHINE_PACKAGE_NAME and MD5 shown in that link to get the latest
version.  
ENV NOMACHINE_PACKAGE_NAME nomachine_5.2.11_1_amd64.deb  
ENV NOMACHINE_MD5 d697e5a565507d522380c94d2f295d07  
  
# Install the mate-desktop-enviroment version you would like to have  
RUN apt-get update -y && \  
apt-get install -y mate-desktop-environment-extras  
  
# Install nomachine, change password and username to whatever you want here  
RUN curl -fSL
"http://download.nomachine.com/download/5.2/Linux/${NOMACHINE_PACKAGE_NAME}"
-o nomachine.deb \  
&& echo "${NOMACHINE_MD5} *nomachine.deb" | md5sum -c - \  
&& dpkg -i nomachine.deb \  
&& groupadd -r nomachine -g 433 \  
&& useradd -u 431 -r -g nomachine -d /home/nomachine -s /bin/bash -c
"NoMachine" nomachine \  
&& adduser nomachine sudo \  
&& mkdir /home/nomachine \  
&& chown -R nomachine:nomachine /home/nomachine \  
&& echo 'nomachine:nomachine' | chpasswd  
  
# install add-apt-repository stuff to get tor-browser working  
RUN apt-get install -y software-properties-common python3-software-properties
python-software-properties wget xdg-utils libpango1.0-0 fonts-liberation  
# download tor and install  
#RUN add-apt-repository ppa:webupd8team/tor-browser  
#RUN apt-get update -y && apt-get install -y tor firefox libreoffice htop nano
git vim tor-browser  
RUN apt-get update -y && apt-get install -y tor firefox libreoffice htop nano
git vim  
  
#ADD nxserver.sh /  
#ENTRYPOINT ["/nxserver.sh"]  
ADD nxserver.sh /nxserver.sh  
RUN chmod 0755 /nxserver.sh  
CMD /nxserver.sh  

