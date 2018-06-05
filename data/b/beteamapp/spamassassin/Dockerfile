FROM debian:jessie  
MAINTAINER Quentin Devos <quentin@qdevos.eu>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
cron \  
libmail-dkim-perl \  
pyzor \  
razor \  
rsyslog \  
spamassassin \  
spamass-milter \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN adduser --shell /bin/false \--home /var/lib/spamassassin \--disabled-
password \--disabled-login \--gecos "" spamd \  
&& usermod -a -G spamd spamass-milter  
  
# Fix an issue in the init script preventing a correct stop of spamass-milter  
COPY ./spamass-milter /etc/init.d/spamass-milter  
COPY ./spamassassin.conf /etc/default/spamassassin  
COPY ./spamass-milter.conf /etc/default/spamass-milter  
COPY ./local.cf /etc/spamassassin/local.cf  
  
RUN echo '## Add TextCat to assist enable language-based filtering' >>
/etc/spamassassin/init.pre \  
&& echo 'loadplugin Mail::SpamAssassin::Plugin::TextCat' >>
/etc/spamassassin/init.pre  
  
# Bootstrap SpamAssassin, Pyzor and Razor  
RUN sa-update \  
&& mkdir /var/lib/spamassassin/.spamassassin \  
&& mkdir /var/lib/spamassassin/.pyzor \  
&& pyzor --homedir=/var/lib/spamassassin/.pyzor discover \  
&& mkdir /var/lib/spamassassin/.razor \  
&& razor-admin -home=/var/lib/spamassassin/.razor -register \  
&& razor-admin -home=/var/lib/spamassassin/.razor -create \  
&& razor-admin -home=/var/lib/spamassassin/.razor -discover \  
&& echo "razorhome = /var/lib/spamassassin/.razor" >>
/var/lib/spamassassin/.razor/razor-agent.conf \  
&& chown -R spamd:spamd /var/lib/spamassassin  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
VOLUME /var/lib/spamassassin  
EXPOSE 12302  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["tail"]

