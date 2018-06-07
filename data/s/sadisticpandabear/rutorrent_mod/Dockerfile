FROM diameter/rtorrent-rutorrent:stable  
USER root  
ADD plimits /var/www/rutorrent/plugins/plimits  
ADD trackers.lst /downloads/.rutorrent/settings/trackers.lst  
RUN chown www-data:www-data /downloads/.rutorrent/settings/trackers.lst &&
chmod 666 /downloads/.rutorrent/settings/trackers.lst && chown -R www-
data:www-data /var/www/rutorrent/plugins/plimits && php
/var/www/rutorrent/php/initplugins.php  

