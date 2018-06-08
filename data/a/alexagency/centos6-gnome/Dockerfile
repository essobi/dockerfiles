FROM alexagency/centos6-xrdp  
MAINTAINER Alex  
  
USER root  
RUN yum -y update && \  
yum -y groupinstall "Fonts" && \  
yum -y install gnome-desktop gnome-panel gnome-session gnome-terminal control-
center \  
nautilus nautilus-open-terminal gedit file-roller samba-client gvfs-smb xdg-
user-dirs && \  
yum clean all && rm -rf /tmp/*  
  
# Configure VNC & XRDP  
RUN sed -i 's/twm /gnome-session /g' /home/user/.vnc/xstartup  
# Applying Gnome Settings for all users  
RUN gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type bool \--set /apps/nautilus/preferences/always_use_browser true && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type bool \--set /apps/gnome-screensaver/idle_activation_enabled false && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type bool \--set /apps/gnome-screensaver/lock_enabled false && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type int \--set /apps/metacity/general/num_workspaces 1 && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type=string \--set /apps/gnome_settings_daemon/keybindings/screensaver ' '
&& \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type=string \--set /apps/gnome_settings_daemon/keybindings/power ' ' && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type bool \--set /apps/panel/global/disable_log_out true && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type int \--set /apps/gnome-power-manager/timeout/sleep_computer_ac '0' &&
\  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type int \--set /apps/gnome-power-manager/timeout/sleep_display_ac '0' && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type int \--set /apps/gnome-screensaver/power_management_delay '0' && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type bool \--set /desktop/gnome/remote_access/enabled true && \  
gconftool-2 \--direct \--config-source
xml:readwrite:/etc/gconf/gconf.xml.mandatory \  
\--type bool \--set /desktop/gnome/remote_access/prompt_enabled false  
# default user  
USER user  
# Creating default user directories  
RUN xdg-user-dirs-update  

