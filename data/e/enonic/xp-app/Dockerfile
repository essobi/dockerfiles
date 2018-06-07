# Base image  
FROM enonic/java8  
  
MAINTAINER Erik Kaareng-sunde <esu@enonic.com>  
  
ENV XP_DISTRO_VERSION 6.14.3  
ENV XP_ROOT /enonic-xp  
ENV XP_HOME /enonic-xp/home  
ENV XP_USER enonic-xp  
ENV XP_UID 1337  
RUN echo "export XP_DISTRO_VERSION=$XP_DISTRO_VERSION" >> /etc/environment  
RUN echo "export XP_ROOT=$XP_ROOT" >> /etc/environment  
RUN echo "export XP_HOME=$XP_HOME" >> /etc/environment  
RUN echo "export XP_USER=$XP_USER" >> /etc/environment  
RUN echo "export XP_UID=$XP_UID" >> /etc/environment  
  
# Install other software  
RUN apt-get -y install wget zip  
  
# Extracting Enonic xp  
RUN wget -O /tmp/distro-$XP_DISTRO_VERSION.zip
http://repo.enonic.com/public/com/enonic/xp/distro/$XP_DISTRO_VERSION/distro-$XP_DISTRO_VERSION.zip  
RUN cd /tmp ; unzip distro-$XP_DISTRO_VERSION.zip  
RUN mv /tmp/enonic-xp-$XP_DISTRO_VERSION/home /tmp/enonic-
xp-$XP_DISTRO_VERSION/home.org  
RUN mkdir -p $XP_ROOT  
RUN cp -rf /tmp/enonic-xp-$XP_DISTRO_VERSION/* $XP_ROOT/.  
  
# Adding Enonic xp user  
RUN adduser --home $XP_ROOT \--gecos "" \--no-create-home --UID $XP_UID
\--disabled-password $XP_USER  
RUN chown -R $XP_USER $XP_ROOT  
# Adding launcher script  
ADD launcher.sh /launcher.sh  
RUN chmod +x /launcher.sh  
  
USER enonic-xp  
  
# Exposing web port, debug port and telnet port  
EXPOSE 8080 5005 5555  
CMD /launcher.sh  

