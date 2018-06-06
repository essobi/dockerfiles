FROM gentoo/portage:latest AS portage  
FROM gentoo/stage3-amd64:latest AS stage3  
  
COPY \--from=portage /usr/portage /usr/portage  
RUN mkdir /etc/portage/repos.conf && cp /usr/share/portage/config/repos.conf
/etc/portage/repos.conf/gentoo.conf  
RUN eselect profile set default/linux/amd64/17.0  
RUN USE="-bindist" emerge -1g openssh  
RUN emerge -g --nospinner --jobs app-portage/layman && emerge -g --oneshot
--nospinner --jobs app-portage/repoman app-portage/gentoolkit && rm -rf
/usr/portage && mkdir /usr/portage && chown portage:portage /usr/portage  
RUN mkdir -p /usr/local/portage/metadata && echo "masters = gentoo" >
/usr/local/portage/metadata/layout.conf  
ADD build.sh /  

