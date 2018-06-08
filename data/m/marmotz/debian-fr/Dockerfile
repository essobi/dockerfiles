FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TIMEZONE Europe/Paris  
  
# Change locale  
RUN apt-get update -y && apt-get install -y locales  
RUN \  
dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
RUN echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen  
  
ENV LC_ALL C.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR.UTF-8  
# Timezone  
RUN echo $TIMEZONE > /etc/timezone && dpkg-reconfigure tzdata  
  
RUN apt-get update -y && apt-get upgrade -y  
  
# Install common dev lib  
RUN apt-get update -y && apt-get install -y build-essential libpng-dev
autoconf automake python-dev  
  
# Install common utils  
RUN apt-get update -y && apt-get install -y git wget curl apt-utils sudo vim
python vim netcat  
COPY wait_service /usr/local/bin/  
  
# Clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# User  
RUN useradd -m -u 1000 nonrootuser  
RUN echo "nonrootuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/nonrootuser  
RUN chmod 0440 /etc/sudoers.d/nonrootuser  
RUN echo '. ~/.bash_aliases' >> /root/.bashrc  
COPY .bash_aliases /root/.bash_aliases  
COPY .bash_aliases /home/nonrootuser/.bash_aliases  
  
USER nonrootuser  
  
CMD ["/bin/bash"]  

