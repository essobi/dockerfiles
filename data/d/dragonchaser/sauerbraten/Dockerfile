FROM opensuse:leap  
MAINTAINER Christian Richter <crichter@suse.com>  
  
  
RUN zypper ref\  
&& zypper --non-interactive up \  
&& zypper --non-interactive in libX11-6 libSDL-1_2-0 libSDL_mixer-1_2-0
libSDL_image-1_2-0 Mesa-libGL1 bzip2 wget tar  
  
RUN wget -qO /usr/local/sauerbraten.tar.bz2
"http://downloads.sourceforge.net/project/sauerbraten/sauerbraten/2013_01_04/sauerbraten_2013_02_03_collect_edition_linux.tar.bz2?r=http%3A%2F%2Fcubeengine.com%2Ffiles.php&ts=1467054652&use_mirror=netcologne"
\  
&& cd /usr/local/ \  
&& tar xvjf /usr/local/sauerbraten.tar.bz2 \  
&& rm /usr/local/sauerbraten.tar.bz2 \  
&& chown -R root:root /usr/local/sauerbraten  
  
RUN wget -qO /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.1/dumb-init_1.1.1_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
  
VOLUME /root/.sauerbraten/  
  
WORKDIR /usr/local/sauerbraten/  
  
EXPOSE 28784/udp 28785/udp 28786/udp  
  
CMD [ "/usr/local/bin/dumb-init", "./sauerbraten_unix", "-yalfredroxx", "-d" ]  

