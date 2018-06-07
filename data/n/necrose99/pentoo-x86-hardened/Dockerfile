FROM necrose99/gentoo-x86-hardened/  
  
MAINTAINER necrose99 necrose99@protmail.ch mike@michaellawrenceit.com  
  
ADD https://raw.githubusercontent.com/alexdux/async-emerge-
overlay/master/async-emerge.conf /etc/portage/repos.conf/async-emerge.conf  
#  
ADD https://www.dropbox.com/s/iwbophp23qo0wp6/image.squashfs?dl=0 /  
# pentoo -x86-hardened root fs squashfs  
RUN layman -S  
RUN eslect profile set pentoo:pentoo/hardened/linux/amd64/bleeding_edge  
RUN pentoo-updater  
  

