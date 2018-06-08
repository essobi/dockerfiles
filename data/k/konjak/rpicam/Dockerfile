FROM resin/rpi-raspbian:stretch  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y supervisor nginx php7.0-fpm php7.0-cli php7.0-common
php-apcu apache2-utils gpac motion zip libav-tools gstreamer1.0-tools \  
alsa-utils mpg321 lame libasound2-dev  
WORKDIR /rpicam  
COPY bin /rpicam/bin  
COPY etc /rpicam/etc  
COPY www /rpicam/www  
COPY config.txt install.sh cam.sh /rpicam/  
RUN chmod o+x *.sh \  
&& sed -i 's/\\[\\[/\\[/g' install.sh \  
&& sed -i 's/\\]\\]/\\]/g' install.sh \  
&& sed -i 's/\\[/\\[\\[/g' install.sh \  
&& sed -i 's/\\]/\\]\\]/g' install.sh \  
&& mkdir -p /opt/vc/bin \  
&& touch /etc/rc.local \  
&& ./install.sh q  
RUN cp etc/asound.conf /etc/asound.conf \  
&& cp etc/supervisor.conf /etc/supervisor.conf \  
&& cp etc/php/7.0/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf \  
&& mkdir -p -m 0777 /run/php \  
&& cp etc/nginx/nginx.conf /etc/nginx/nginx.conf \  
&& sed -i -e "s/defaults.ctl.card 0/defaults.ctl.card 1/g"
/usr/share/alsa/alsa.conf \  
&& sed -i -e "s/defaults.pcm.card 0/defaults.pcm.card 1/g"
/usr/share/alsa/alsa.conf  
COPY docker-entrypoint.sh /rpicam/  
RUN chmod u+x docker-entrypoint.sh  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["supervisord", "-c", "/etc/supervisor.conf"]  

