FROM vguardiola/gentoo  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
COPY ./etc/portage/package.use/nginx /etc/portage/package.use/nginx  
COPY ./etc/locale.nopurge /etc/locale.nopurge  
RUN emerge -D www-servers/nginx && eclean-dist -dqf && localepurge && rm
/usr/portage/distfiles -rf  
COPY ./etc/security/limits.d/nginx /etc/security/limits.d/nginx  
RUN geoipupdate.sh -f  
RUN chown nobody:nginx /var/lib/nginx/tmp  
EXPOSE 80 8000  
CMD ["nginx", "-g", "daemon off;"]  

