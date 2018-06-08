FROM nerka/docker-dokuwiki:alpine_edge_simple_1.3  
MAINTAINER Xavier Godon <xav.godon@gmail.com>  
  
RUN cd /var/www/lib/plugins/ && \  
curl -O -L "https://github.com/samuelet/indexmenu/archive/master.zip" && \  
unzip master.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/indexmenu-master /var/www/lib/plugins/indexmenu && \  
rm -rf master.zip  
  
RUN cd /var/www/lib/plugins/ && \  
curl -O -L "https://github.com/LarsGit223/dokuwiki-plugin-
odt/archive/master.zip" && \  
unzip master.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/dokuwiki-plugin-odt-master /var/www/lib/plugins/odt &&
\  
rm -rf master.zip  
  
RUN cd /var/www/lib/plugins/ && \  
curl -O -L "https://github.com/michitux/dokuwiki-plugin-
text/archive/master.zip" && \  
unzip master.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/dokuwiki-plugin-text-master /var/www/lib/plugins/text
&& \  
rm -rf master.zip  
  
RUN cd /var/www/lib/plugins/ && \  
curl -O -L "https://github.com/splitbrain/dokuwiki-plugin-
smtp/archive/master.zip" && \  
unzip master.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/dokuwiki-plugin-smtp-master /var/www/lib/plugins/smtp
&& \  
rm -rf master.zip  
  
RUN cd /var/www/lib/plugins/ && \  
curl -O -L "https://github.com/splitbrain/dokuwiki-plugin-
dw2pdf/archive/master.zip" && \  
unzip master.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/dokuwiki-plugin-dw2pdf-master
/var/www/lib/plugins/dw2pdf && \  
rm -rf master.zip  
  
RUN cd /var/www/lib/plugins/ && \  
curl -O -L "https://github.com/Klap-in/dokuwiki-plugin-
bookcreator/archive/master.zip" && \  
unzip master.zip -d /var/www/lib/plugins/ && \  
mv /var/www/lib/plugins/dokuwiki-plugin-bookcreator-master
/var/www/lib/plugins/bookcreator && \  
rm -rf master.zip  
  
  

