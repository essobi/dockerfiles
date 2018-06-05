FROM ubuntu:trusty  
  
#echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo
tee /etc/apt/sources.list.d/mono-xamarin.list \  
  
RUN \  
echo "deb http://download.mono-project.com/repo/debian nightly main" | sudo
tee /etc/apt/sources.list.d/mono-nightly.list \  
&& echo "postfix postfix/main_mailer_type string Internet site" > preseed.txt
\  
&& echo "postfix postfix/mailname string mailmirror.silvenga.com" >>
preseed.txt \  
&& debconf-set-selections preseed.txt \  
  
&& DEBIAN_FRONTEND=noninteractive apt-key adv --keyserver
hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
mono-runtime \  
"^libmono-system.*4\\.0-cil$" \  
postfix \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
echo "piper unix - n n - - pipe" >> /etc/postfix/master.cf \  
&& echo " flags=X user=piper argv=/usr/bin/mono /opt/MailMirror.Net.Piper.exe
id test test" >> /etc/postfix/master.cf \  
&& useradd piper \  
&& postconf -e mynetworks="0.0.0.0/0" \  
&& postconf -e default_transport="piper"  
  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q \  
wget \  
unzip \  
  
&& wget -P /tmp/ https://ci.appveyor.com/api/projects/Silvenga/mailmirror-
net/artifacts/src/MailMirror.Net.Api/bin/api.zip \  
&& wget -P /tmp/ https://ci.appveyor.com/api/projects/Silvenga/mailmirror-
net/artifacts/src/MailMirror.Net.Piper/bin/piper.zip \  
&& wget -P /tmp/ https://ci.appveyor.com/api/projects/Silvenga/mailmirror-
net/artifacts/src/MailMirror.Net.Site/site.zip \  
  
&& unzip -o /tmp/api.zip -d /opt/ \  
&& unzip -o /tmp/piper.zip -d /opt/ \  
&& unzip -o /tmp/site.zip -d /opt/wwwroot/ \  
  
&& rm /tmp/* \  
&& apt-get purge -y \  
wget \  
unzip \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 25 9000  
  
ADD start.sh /opt/  
CMD /bin/bash /opt/start.sh

