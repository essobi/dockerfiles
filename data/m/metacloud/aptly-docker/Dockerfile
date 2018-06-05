FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install aptly and required tools  
RUN apt-get -q update \  
&& apt-get -y install bash-completion \  
bzip2 \  
gnupg \  
gpgv \  
graphviz \  
wget \  
xz-utils \  
&& echo "deb http://repo.aptly.info/ squeeze main" >
/etc/apt/sources.list.d/aptly.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9E3E53F19C7DE460 \  
&& apt-get -q update \  
&& apt-get -y install aptly  
  
COPY aptly.conf /etc/aptly.conf  
COPY entrypoint.sh /entrypoint.sh  
  
# Enable Aptly Bash completions  
RUN wget
https://raw.githubusercontent.com/smira/aptly/master/bash_completion.d/aptly \  
-O /etc/bash_completion.d/aptly \  
&& echo "if ! shopt -oq posix; then\n\  
if [ -f /usr/share/bash-completion/bash_completion ]; then\n\  
. /usr/share/bash-completion/bash_completion\n\  
elif [ -f /etc/bash_completion ]; then\n\  
. /etc/bash_completion\n\  
fi\n\  
fi" >> /etc/bash.bashrc  
  
VOLUME ["/var/lib/aptly"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]  

