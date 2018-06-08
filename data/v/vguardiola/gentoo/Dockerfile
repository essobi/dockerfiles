FROM vguardiola/gentoo-amd64  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
COPY ./etc/portage/repos.conf/gentoo.conf /etc/portage/repos.conf/gentoo.conf  
RUN echo "LINGUAS=\"en\"" >> /etc/portage/make.conf  
RUN echo "FEATURES=\"${FEATURES} noman noinfo nodoc\"" >>
/etc/portage/make.conf  
RUN echo "EMERGE_DEFAULT_OPTS=\"${EMERGE_DEFAULT_OPTS} -q --jobs 4\"" >>
/etc/portage/make.conf  
RUN echo "PORTAGE_RSYNC_EXTRA_OPTS=\"--exclude-
from=/etc/portage/rsync_excludes\"" >> /etc/portage/make.conf  
COPY ./etc/portage/rsync_excludes /etc/portage/rsync_excludes  
COPY ./etc/locale.nopurge /etc/locale.nopurge  
RUN emerge-webrsync && emerge app-portage/eix app-portage/gentoolkit && eix-
update \  
&& emerge -D app-misc/ca-certificates app-admin/localepurge emerge app-
portage/layman && localepurge && etc-update --automode -5 && rm
/usr/portage/distfiles -rf  
COPY ./etc/layman/layman.cfg /etc/layman/layman.cfg  
RUN echo "source /var/lib/layman/make.conf" >> /etc/portage/make.conf  
RUN layman -S && layman -a vgl-devops  
COPY ./etc/locale.nopurge /etc/locale.nopurge  

