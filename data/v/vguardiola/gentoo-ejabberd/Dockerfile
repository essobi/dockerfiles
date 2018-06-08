FROM vguardiola/gentoo  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
COPY ./etc/portage/package.keywords/ejabberd
/etc/portage/package.keywords/ejabberd  
COPY ./etc/portage/package.use/ejabberd /etc/portage/package.use/ejabberd  
RUN eix-update && emerge -D dev-lang/erlang =net-im/ejabberd-16.09 && eclean-
dist -dqf && localepurge && rm /usr/portage/distfiles -rf  
COPY ./etc/jabber/ejabberdctl.cfg /etc/jabber/ejabberdctl.cfg  
RUN ejabberdctl start && sleep 5 && ejabberdctl modules_update_specs &&
ejabberdctl module_install ejabberd_auth_http \  
&& ejabberdctl module_install mod_pottymouth && ejabberdctl module_install
mod_archive && ejabberdctl stop  
COPY ./etc/jabber/ejabberd-modules/conf/mod_pottymouth.yml
/etc/jabber/ejabberd-modules/conf/mod_pottymouth.yml  
COPY ./etc/jabber/badwords/blacklist.en.txt
/etc/jabber/badwords/blacklist.en.txt  
COPY ./etc/jabber/badwords/blacklist.es.txt
/etc/jabber/badwords/blacklist.es.txt  
EXPOSE 5222 5269 5280  
CMD ["ejabberdctl", "foreground"]

