FROM alpine:3.4  
  
RUN apk add --no-cache clamav-daemon clamav-scanner clamav-libunrar rsync wget
curl gnupg git tini bash bind-tools  
  
ADD . /tmp/build-src/  
RUN mkdir /run/clamav/ \  
&& chown clamav:clamav /run/clamav \  
&& cp /tmp/build-src/clamd.conf /etc/clamav/clamd.conf \  
&& sed -i 's#/var/lib/clamav#/data/clamav#' /etc/clamav/freshclam.conf \  
  
&& git clone https://github.com/extremeshok/clamav-unofficial-sigs/
/tmp/clamav-unofficial-sigs/ \  
&& mkdir -p /usr/local/bin/ /var/log/clamav-unofficial-sigs/ /etc/clamav-
unofficial-sigs/ \  
&& cp /tmp/clamav-unofficial-sigs/clamav-unofficial-sigs.sh
/usr/local/bin/clamav-unofficial-sigs.sh \  
&& chmod +x /usr/local/bin/clamav-unofficial-sigs.sh \  
&& cp /tmp/clamav-unofficial-sigs/config/*.* /etc/clamav-unofficial-sigs/ \  
&& cp /tmp/build-src/os.docker.conf /etc/clamav-unofficial-sigs/os.conf \  
&& chown clamav:clamav /etc/clamav-unofficial-sigs/os.conf \  
  
&& cp /tmp/build-src/start.sh /usr/local/bin/start.sh \  
&& chmod +x /usr/local/bin/start.sh \  
  
&& rm -Rf /tmp/clamav-unofficial-sigs /tmp/build-src  
  
USER clamav  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/usr/local/bin/start.sh"]  

