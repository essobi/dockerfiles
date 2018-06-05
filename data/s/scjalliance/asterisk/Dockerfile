FROM respoke/asterisk:14  
  
VOLUME /etc/asterisk  
VOLUME /var/lib/asterisk/licenses  
  
RUN curl -sL -o /usr/sbin/digium-register
http://downloads.digium.com/pub/register/x86-32/register  
RUN curl -sL
http://downloads.digium.com/pub/telephony/res_digium_phone/asterisk-14.0/x86-64/res_digium_phone-
bundled-14.0_current-x86_64.tar.gz | tar -C /usr/lib/asterisk/modules
\--wildcards \--strip-components 1 -xz res_*.so  

