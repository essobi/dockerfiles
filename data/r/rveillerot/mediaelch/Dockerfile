FROM jlesage/baseimage-gui:ubuntu-16.04-v3  
  
# Add MediaElch Repo  
RUN echo deb http://ppa.launchpad.net/kvibes/mediaelch/ubuntu xenial main >>
/etc/apt/sources.list.d/mediaelch.list  
RUN echo deb-src http://ppa.launchpad.net/kvibes/mediaelch/ubuntu xenial main
>> /etc/apt/sources.list.d/mediaelch.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 00DAEE81 && apt-
get update  
  
# Install MediaElch  
RUN apt-get install -y mediaelch qtdeclarative5-models-plugin qml-module-
qtquick-controls libqt5multimedia5-plugins  
  
# Install SSH server  
#RUN apt-get install -y openssh-server  
#RUN mkdir /var/run/sshd  
# Create user  
RUN adduser --disabled-password --gecos "" mediaelch  
  
# Configuration SSH  
#RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin no/'
/etc/ssh/sshd_config  
#RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
#RUN mkdir -p /home/mediaelch/.ssh && chown mediaelch:mediaelch
/home/mediaelch/.ssh && chmod 700 /home/mediaelch/.ssh  
# Entrypoint  
COPY entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
RUN apt-get install -y locales  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN echo 'export LC_ALL=en_US.UTF-8' >> /home/mediaelch/.profile  
RUN echo 'export LANG=en_US.UTF-8' >> /home/mediaelch/.profile  
RUN echo 'export LANGUAGE=en_US.UTF-8' >> /home/mediaelch/.profile  
RUN echo 'export LC_ALL=en_US.UTF-8' >> /home/mediaelch/.bashrc  
RUN echo 'export LANG=en_US.UTF-8' >> /home/mediaelch/.bashrc  
RUN echo 'export LANGUAGE=en_US.UTF-8' >> /home/mediaelch/.bashrc  
  
#EXPOSE 22  
#VOLUME /movies /shows /home/mediaelch/.config/kvibes
/home/mediaelch/.ssh/authorized_keys  
# Define mountable directories.  
ENV APP_NAME="MediaElch"  
VOLUME ["/movies"]  
VOLUME ["/home/mediaelch/.config/kvibes"]  
  
COPY startapp.sh /startapp.sh  
  
#ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
#CMD ["/usr/sbin/sshd", "-D"]  

