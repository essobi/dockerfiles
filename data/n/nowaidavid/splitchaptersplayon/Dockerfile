FROM ubuntu:14.04  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install software-properties-common -y && apt-get install unzip -y  
RUN add-apt-repository ppa:mc3man/trusty-media  
RUN apt-get update -y  
RUN apt-get install ffmpeg -y  
RUN apt-get install python3 -y && apt-get install python3-pip -y && apt-get
install python -y && apt-get install python-pip -y  
  
# Speed up APT  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# Remove built-in Java 7  
RUN apt-get purge -y openjdk-\\* icedtea\\*  
  
# Auto-accept Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# Filebot needs Java 8  
RUN add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get clean  
  
# To find the latest version:
https://www.filebot.net/download.php?mode=s&type=deb&arch=amd64  
# We'll use a specific version for reproducible builds  
RUN set -x \  
&& wget -N
'https://sourceforge.net/projects/filebot/files/filebot/FileBot_4.7.8/filebot_4.7.8_amd64.deb'
-O /root/filebot.deb \  
&& dpkg -i /root/filebot.deb && rm /root/filebot.deb \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD chapter_split.py /tmp/chapter_split.py  
CMD ["python", "/tmp/chapter_split.py", "-f", "/convertfiles/input.mp4"]  
  
#filebot -rename convertfiles/output --db TheTVDB --format {n} - {s00e00} -
{t} --action move --conflict override  

