FROM node:slim  
  
ENV ARCH=amd64  
  
RUN apt-get update \  
&& apt-get install -y apt-utils locales \  
&& apt-get install -y curl tzdata libav-tools python-dev python3-dev python-
setuptools python3-setuptools mc locales cron \  
&& locale-gen en_US.UTF-8 \  
&& curl -SLO "https://github.com/just-
containers/s6-overlay/releases/download/v1.20.0.0/s6-overlay-${ARCH}.tar.gz" \  
&& tar -xzf s6-overlay-amd64.tar.gz -C / \  
&& tar -xzf s6-overlay-amd64.tar.gz -C /usr ./bin \  
&& rm -rf s6-overlay-amd64.tar.gz \  
&& useradd -u 911 -U -d /config -s /bin/false abc \  
&& usermod -G users abc \  
&& mkdir -p /app /config /defaults \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* \  
&& easy_install3 pip \  
&& pip install requests youtube-dl  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
COPY rootfs /  
  
RUN chmod +x /etc/services.d/cron/run  
  
ENTRYPOINT [ "/init" ]  

