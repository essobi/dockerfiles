FROM alpine:3.6  
RUN adduser -S mopidy  
  
# Default configuration  
COPY mopidy.conf /home/mopidy/.config/mopidy/mopidy.conf  
  
# Start helper script  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk update \  
&& apk upgrade \  
  
&& apk add \--no-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/main \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
gstreamer \  
mopidy=2.1.0-r1 \  
py-pip=9.0.1-r1 \  
python-dev alpine-sdk \  
  
&& if [[ ! -e /usr/bin/easy_install ]]; then ln -sf /usr/bin/easy_install-3.4
/usr/bin/easy_install; fi \  
&& pip install --upgrade pip \  
&& if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3.4 /usr/bin/pip; fi \  
&& pip install -U six \  
&& pip install Mopidy-GMusic Mopidy-Youtube youtube-dl pyasn1  
  
RUN chown mopidy:audio -R /etc/mopidy \  
&& chown mopidy:audio /entrypoint.sh  
  
# Run as mopidy user  
USER mopidy  
  
CMD ["/usr/bin/mopidy"]  

