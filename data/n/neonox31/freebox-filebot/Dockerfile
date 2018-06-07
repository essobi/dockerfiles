# ----------------------------------------------------  
# Inspired by https://github.com/coppit/docker-filebot  
# ----------------------------------------------------  
FROM phusion/baseimage:0.9.19  
MAINTAINER Logan WEBER <weberlogan@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Speed up APT  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# Auto-accept Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Filebot needs Java 8 and mediainfo library  
RUN add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get install -y libmediainfo-dev  
  
# Install jq for freebox script  
RUN apt-get install -y jq  
  
# Install dos2unix  
RUN apt-get install -y dos2unix  
  
# Create dir to keep things tidy. Make sure it's readable by $USER_ID  
RUN mkdir /files  
RUN chmod a+rwX /files  
  
RUN set -x \  
&& wget -O /files/filebot.deb
'https://app.filebot.net/download.php?type=deb&arch=amd64&version=4.7.7' \  
&& dpkg -i /files/filebot.deb && rm /files/filebot.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/freebox", "/completed", "/output", "/config"]  
  
# Rev-locking this to ensure reproducible builds  
RUN wget -O /files/runas.sh \  
'https://raw.githubusercontent.com/coppit/docker-inotify-
command/7be05137c367a7bbff6b7980aa14e8af0c24eca6/runas.sh'  
RUN chmod a+wx /files/runas.sh  
  
# Get freeboxOS API script  
RUN wget -O /files/freeboxos_bash_api.sh \  
'http://github.com/JrCs/freeboxos-bash-api/raw/master/freeboxos_bash_api.sh'  
RUN chmod a+wx /files/freeboxos_bash_api.sh  
  
# Add scripts. Make sure scripts and confs are executable by $USER_ID  
ADD pre-run.sh /files/pre-run.sh  
RUN chmod a+x /files/pre-run.sh  
RUN dos2unix /files/pre-run.sh  
ADD start.sh /files/start.sh  
RUN chmod a+x /files/start.sh  
RUN dos2unix /files/start.sh  
ADD filebot.sh /files/filebot.sh  
RUN chmod a+wx /files/filebot.sh  
RUN dos2unix /files/filebot.sh  
ADD filebot.conf /files/filebot.conf  
RUN chmod a+wx /files/filebot.conf  
ADD freebox.sh /files/freebox.sh  
RUN chmod a+wx /files/freebox.sh  
RUN dos2unix /files/freebox.sh  
ADD freebox.conf /files/freebox.conf  
RUN chmod a+wx /files/freebox.conf  
  
ENV USER_ID 0  
ENV GROUP_ID 0  
ENV UMASK 0000  
CMD /files/start.sh  

