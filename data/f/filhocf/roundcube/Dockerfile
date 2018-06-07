FROM roundcube/roundcubemail  
  
MAINTAINER Claudio Ferreira <filhocf@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Get Extra Plugins and Skins packages  
WORKDIR /usr/src/roundcubemail/  
RUN \  
# Get plugin  
# Context Menu  
mkdir -p plugins/contextmenu; \  
curl -L https://github.com/johndoh/roundcube-contextmenu/archive/master.tar.gz
| \  
tar xz --strip-components=1 -C plugins/contextmenu; \  
# Context Menu Folder  
mkdir -p plugins/contextmenu_folder; \  
curl -L https://github.com/random-
cuber/contextmenu_folder/archive/master.tar.gz | \  
tar xz --strip-components=1 -C plugins/contextmenu_folder; \  
# Message Highlight  
mkdir -p plugins/message_highlight; \  
curl -L https://github.com/corbosman/message_highlight/archive/master.tar.gz |
\  
tar xz --strip-components=1 -C plugins/message_highlight; \  
#Infinte Scroll  
mkdir -p plugins/infinitescroll; \  
curl -L https://github.com/messagerie-melanie2/Roundcube-Plugin-Infinite-
Scroll/archive/master.tar.gz | \  
tar xz --strip-components=1 -C plugins/infinitescroll; \  
# Thunderbird Labels  
mkdir -p plugins/thunderbird_labels; \  
curl -L https://github.com/mike-kfed/rcmail-thunderbird-
labels/archive/master.tar.gz | \  
tar xz --strip-components=1 -C plugins/thunderbird_labels; \  
# Remove Attachments  
mkdir -p plugins/removeattachments; \  
curl -L https://github.com/dsoares/Roundcube-Plugin-
RemoveAttachments/archive/master.tar.gz -O removeattach.tar.gz; \  
tar xz --strip-components=1 -C plugins/removeattachments; \  
# Remove Attach Position  
mkdir -p plugins/attachment_position; \  
#curl -L https://github.com/dapphp/Roundcube-Plugin-
attachment_position/archive/1.0.0.tar.gz -O attachposition.tar.gz; \  
curl -L https://github.com/filhocf/roundcube-
attachment_position/archive/master.tar.gz | \  
tar xz --strip-components=1 -C plugins/attachment_position; \  
# HTML5 Notifier  
mkdir -p plugins/html5_notifier; \  
curl -L https://github.com/filhocf/roundcube-
html5_notifier/archive/master.tar.gz | \  
tar xz --strip-components=1 -C plugins/html5_notifier; \  
# Get themes  
# Mabola Blue theme  
mkdir -p skins/mabola; \  
curl -L https://github.com/filhocf/mabola/archive/master.tar.gz | \  
tar xz --strip-components=1 -C skins/mabola; \  
# Mabola theme  
mkdir -p skins/mabola-blue; \  
curl -L https://github.com/EstudioNexos/mabola-blue/archive/master.tar.gz | \  
tar xz --strip-components=1 -C skins/mabola-blue; \  
# Chameleon theme  
mkdir -p skins/chameleon; \  
curl -L https://github.com/filhocf/roundcube-chameleon/archive/master.tar.gz |
\  
tar xz --strip-components=1 -C skins/chameleon; \  
# Chameleon Blue theme  
mkdir -p skins/chameleon-blue; \  
curl -L https://github.com/filhocf/roundcube-chameleon-
blue/archive/master.tar.gz | \  
tar xz --strip-components=1 -C skins/chameleon-blue; \  
cd plugins; \  
echo "Add Kolab's plugin ===============>>>>>>>>>>>>>"; \  
curl -L https://github.com/filhocf/roundcubemail-plugins-
kolab/archive/master.tar.gz | \  
tar xz && \  
mv roundcubemail-plugins-kolab-master roundcube-plugins; \  
ln -s roundcube-plugins/plugins/calendar; \  
ln -s roundcube-plugins/plugins/libcalendaring; \  
ln -s roundcube-plugins/plugins/piwik_analytics; \  
ln -s roundcube-plugins/plugins/tasklist  
  
WORKDIR /var/www/html  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

