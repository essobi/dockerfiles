FROM opensuse:leap  
MAINTAINER Christian Richter <crichter@suse.com>  
  
  
RUN zypper ref\  
&& zypper --non-interactive up \  
&& zypper --non-interactive in libX11-6 libSDL-1_2-0 libSDL_mixer-1_2-0
libSDL_image-1_2-0 Mesa-libGL1 bzip2 wget tar  
  
RUN wget -qO /usr/local/teeworlds.tar.gz
https://github.com/teeworlds/teeworlds/releases/download/0.6.4-release/teeworlds-0.6.4-linux_x86_64.tar.gz
\  
&& cd /usr/local/ \  
&& tar xfvz /usr/local/teeworlds.tar.gz \  
&& rm /usr/local/teeworlds.tar.gz \  
&& mv teeworlds-0.6.4-linux_x86_64 teeworlds \  
&& chown -R root:root /usr/local/teeworlds  
  
RUN wget -qO /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.1/dumb-init_1.1.1_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
  
VOLUME /root/.teeworlds/  
  
WORKDIR /usr/local/teeworlds/  
  
EXPOSE 8303/udp  
COPY autoexec.cfg /usr/local/teeworlds/  
CMD [ "/usr/local/bin/dumb-init", "./teeworlds_srv"]  

