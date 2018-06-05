FROM ubuntu:xenial  
  
WORKDIR /opt/comba  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.2.list  
  
RUN apt-get update && apt-get install -y --allow-unauthenticated \  
git \  
curl \  
python \  
libpython-dev \  
python-dev \  
python-examples \  
alsa-base \  
liquidsoap \  
liquidsoap-plugin-xmlplaylist \  
liquidsoap-plugin-alsa \  
liquidsoap-plugin-samplerate \  
python-pip \  
python-redis \  
python-simplejson \  
python-logutils \  
python-chardet \  
redis-server \  
libev4 \  
libev-dev \  
mongodb-org \  
sox \  
libcurl4-openssl-dev \  
libsox-fmt-mp3 \  
supervisor \  
libffi-dev \  
libssl-dev \  
bc \  
quelcom \  
netcat \  
ssmtp \  
mailutils \  
gettext-base \  
tzdata  
  
RUN echo "deb
http://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-
stable/Debian_9.0/ ./" >> /etc/apt/sources.list && \  
wget
https://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-
stable/Debian_9.0/Release.key -O- | apt-key add && \  
apt-get install -y \  
libzmq3-dev  
  
RUN wget -O - http://tools.janguo.de/repos/apt/tools.janguo.de.key|apt-key add
-  
  
RUN cd /opt/ && rm -Rf comba && \  
git clone https://gitlab.janguo.de/comba/comba_main.git comba && \  
cd /opt/comba && \  
git fetch origin;git reset --hard HEAD  
  
RUN cd /opt/comba && \  
sed -i "s/:/\//g" .gitmodules  
RUN cd /opt/comba && \  
sed -i "s/git@/https:\/\//g" .gitmodules  
RUN cd /opt/comba && \  
git submodule sync && \  
git submodule update --init  
  
RUN LIQUIDGROUP=$(cat /etc/init.d/liquidsoap | grep "group=") && \  
LIQUIDGROUP=${LIQUIDGROUP#*\=} && \  
if ! id comba >/dev/null 2>&1; then \  
adduser --quiet --system --disabled-password --disabled-login --uid 678 \  
\--home /opt/comba --ingroup $LIQUIDGROUP comba \  
&& usermod -a -G audio comba; \  
fi  
RUN audio_folders='fallback archive jingles preprod rec'; \  
for folder in $audio_folders; do \  
mkdir -p "/var/audio/$folder"; \  
chmod 775 "/var/audio/$folder"; \  
done;  
  
RUN mkdir -p /var/run/comba && chown comba:liquidsoap /var/run/comba;  
RUN mkdir -p /etc/comba && cp /opt/comba/data/deployment/etc/comba/comba.ini
/etc/comba/comba.ini  
RUN cp /opt/comba/data/deployment/etc/comba/scheduler.xml
/etc/comba/scheduler.xml  
ADD assets/dummy.wav /var/audio/fallback/dummy.wav  
RUN mkdir -p /opt/comba/var/audio/  
ADD assets/dummy.wav /opt/comba/var/audio/dummy.wav  
  
RUN LIQUIDGROUP=$(cat /etc/init.d/liquidsoap | grep "group="); \  
LIQUIDGROUP=${LIQUIDGROUP#*\=}; \  
chown -R comba:$LIQUIDGROUP /var/audio; \  
chmod 774 /opt/comba/combac.py; \  
chmod 774 /opt/comba/combas.py; \  
chmod 774 /opt/comba/combaa.py; \  
chown comba /opt/comba/combac.py; \  
chown comba /opt/comba/combas.py; \  
chown comba /opt/comba/combaa.py; \  
chown comba /etc/comba/scheduler.xml; \  
chown -R comba:$LIQUIDGROUP /opt/comba/soundengine/helpers; \  
chmod 774 /opt/comba/soundengine/helpers/silence.sh; \  
[ ! -d /var/log/comba ] && mkdir /var/log/comba && chown -R comba:$LIQUIDGROUP
/var/log/comba && chmod 775 /var/log/comba; \  
[ ! -d /var/log/pyweb ] && mkdir /var/log/pyweb && touch
/var/log/pyweb/pyweb.log && chown -R comba:$LIQUIDGROUP /var/log/pyweb &&
chmod 775 /var/log/pyweb; \  
[ ! -d /usr/lib/python2.7/config ] && find /usr/lib/python2.7/ -maxdepth 1
-type d -name "config*" -print | head -1| xargs -i -n1 ln -s {}
/usr/lib/python2.7/config; \  
[ ! -d /tmp/comba ] && mkdir /tmp/comba; \  
if [ ! -f /usr/bin/combapasswd ]; then cd /tmp/comba && python
/usr/share/doc/python2.7/examples/Tools/freeze/freeze.py
/opt/comba/tools/combapasswd && make && cp combapasswd /usr/bin; fi; \  
if [ ! -f /usr/bin/combawhitelist ]; then cd /tmp/comba && export
PYTHONPATH=$PYTHONPATH:/opt/comba/libraries && python
/usr/share/doc/python2.7/examples/Tools/freeze/freeze.py
/opt/comba/tools/combawhitelist
/opt/comba/libraries/comba_lib/security/whitelist.py && make && cp
combawhitelist /usr/bin; fi;\  
if [ ! -f /usr/bin/comba-cfg ]; then cd /tmp/comba && python
/usr/share/doc/python2.7/examples/Tools/freeze/freeze.py
/opt/comba/tools/comba-cfg && make && cp comba-cfg /usr/bin; fi; \  
if [ ! -f /usr/bin/combamessage ]; then cd /tmp/comba && export
PYTHONPATH=$PYTHONPATH:/opt/comba/libraries && python
/usr/share/doc/python2.7/examples/Tools/freeze/freeze.py
/opt/comba/tools/combamessage
/opt/comba/libraries/comba_lib/reporting/messenger.py
/opt/comba/libraries/comba_lib/reporting/statestore.py -m encodings && make &&
cp combamessage /usr/bin; fi;  
  
RUN [ -d /tmp/comba ] && rm -Rf /tmp/comba; \  
cd /opt/comba/; \  
rm -Rf clientapi; \  
rm -Rf libraries; \  
rm -Rf services; \  
rm -Rf web/comba_web_api; \  
rm -Rf web/comba_web_monitor; \  
rm -Rf web/comba_web_programme;  
  
RUN mkdir -p /var/log/comba/  
RUN mkdir -p /opt/comba/var/sqlite && chown comba /opt/comba/var/sqlite  
  
RUN pip install --upgrade pip && pip install -r
/opt/comba/data/requirements.txt && \  
pip install "pyzmq>=16.0.2" \--upgrade --install-option="--zmq=bundled"  
  
ADD etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD etc/ssmtp.conf /etc/ssmtp/ssmtp.template  
  
ADD etc/comba.ini /etc/comba/comba.template  
  
RUN sh -c 'echo "bind_ip = 127.0.0.1" >> /etc/mongodb.conf'  
  
RUN mkdir -p /var/redis/data && \  
sed -i s@^daemonize\ .*@daemonize\ no@g /etc/redis/redis.conf && \  
sed -i s@^dir\ .*@dir\ /var/redis/data/@g /etc/redis/redis.conf && \  
sed -i s/^bind\ .*$/bind\ 127\\.0\\.0\\.1/g /etc/redis/redis.conf  
RUN chown -R comba /opt/comba/web && touch /var/log/comba/web.log && chown
comba /var/log/comba/web.log;  
  
ADD entrypoint /usr/local/bin/entrypoint  
  
RUN mkdir -p /data/db  
ENV COMBA_WEB_ADMIN "comba"  
ENV COMBA_WEB_ADMIN_PASSWORD "comba"  
ENV MAILHUB "mail.server.tld"  
ENV MAILUSER "itsyou"  
ENV MAILPASSWORD "secret"  
ENV MAILUSETLS "YES"  
ENV MAILUSESTARTTLS "YES"  
ENV ALSA_BUFFER "16384"  
ENV ADMINMAILTO "admin@mydomain.tld"  
ENV ADMINMAILFROM "comba@mydomain.tld"  
ENV CALENDERURL "http://bermudafunk-
kalender.critmass.de/index.php?option=com_jimtawl&view=calendar&format=json&from=#datefrom#&to=#dateto#"  
ENV RECORDERINPUT "soundcard"  
ENV ALTRECORDERINPUT "nosound"  
ENV RECORDERDEVICE "default"  
ENV ALTRECORDERDEVICE "none"  
ENV PLAYERDEVICE "default"  
ENV PLAYER_INPUT "fallback"  
ENV WEBSERVICEPORT "8000"  
ENV COMBA_CONTROLLER_PORT "9099"  
ENV STREAMING "n"  
ENV STREAM_ADMIN "admin"  
ENV STREAM_ADMIN_PASSWORD ""  
ENV STREAM_HOST ""  
ENV STREAM_NAME ""  
ENV STREAM_PASSWORD ""  
ENV STREAM_MOUNTPOINT ""  
ENV STREAM_PORT ""  
ENV STREAM_USER ""  
ENV STREAM_URL ""  
ENV STREAM_BITRATE "128"  
ENV STREAM_GENRE "Mixed"  
ENV STREAM_DESCRIPTION "Radio Stream"  
ENV STREAM_TYPE "icecast"  
ENV USERID ""  
ENV COMBA_TIMEZONE Europe/Berlin  
  
EXPOSE 8000 9099  
ENTRYPOINT /usr/local/bin/entrypoint  
CMD ["/usr/bin/supervisord", "-n"]  
  

