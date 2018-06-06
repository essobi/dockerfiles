FROM library/ubuntu:bionic AS build  
  
ENV LANG=C.UTF-8  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
software-properties-common \  
apt-utils  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y \  
wget  
  
RUN mkdir /build /rootfs  
WORKDIR /build  
RUN wget -nv
https://github.com/krallin/tini/releases/download/v0.18.0/tini_0.18.0-amd64.deb  
RUN apt-get download \  
libselinux1 \  
libsemanage1 \  
libsemanage-common \  
libsepol1 \  
libpam0g \  
libpam-modules \  
libpam-modules-bin \  
libaudit1 \  
libaudit-common \  
libcap-ng0 \  
libbz2-1.0 \  
libdb5.3 \  
libpcre3 \  
libustr-1.0-1 \  
libpam-runtime \  
sudo \  
passwd \  
cron  
RUN find *.deb | xargs -I % dpkg-deb -x % /rootfs  
  
WORKDIR /rootfs  
RUN rm -rf \  
etc/cron*/* \  
etc/cron*/.placeholder \  
etc/default/* \  
etc/init \  
etc/init.d \  
etc/security/namespace.init \  
etc/*/README \  
sbin/shadowconfig \  
lib/systemd \  
usr/bin/tini-static \  
usr/include \  
usr/lib/tmpfiles.d \  
usr/lib/sudo/*.la \  
usr/sbin/pam* \  
usr/share/apport \  
usr/share/bug \  
usr/share/doc \  
usr/share/lintian \  
usr/share/man \  
usr/share/pam/*.md5sums \  
&& mkdir -p \  
etc/skel \  
&& sed -i -r \  
's,test -x /usr/sbin/anacron [|][|] [(] | [)],,g' \  
etc/crontab \  
&& sed -i -r \  
-e '/^ *%.*$/d' \  
-e 's,:/snap/bin,,g' \  
-e '/^[[:space:]]*Defaults[[:space:]]+mail_badpass.*$/d' \  
etc/sudoers \  
&& sed \  
-e 's/\$account_primary/account [success=1 new_authtok_reqd=done default=ignore] pam_unix.so/g' \  
-e 's/\$account_additional//g' \  
usr/share/pam/common-account > etc/pam.d/common-account \  
&& sed \  
-e 's/\$auth_primary/auth [success=1 default=ignore] pam_unix.so nullok_secure/g' \  
-e 's/\$auth_additional//g' \  
usr/share/pam/common-auth > etc/pam.d/common-auth \  
&& sed \  
-e 's/\$password_primary/password [success=1 default=ignore] pam_unix.so obscure sha512/g' \  
-e 's/\$password_additional//g' \  
usr/share/pam/common-password > etc/pam.d/common-password \  
&& sed \  
-e 's/\$session_primary/session [default=1] pam_permit.so/g' \  
-e 's/\$session_additional/session required pam_unix.so/g' \  
usr/share/pam/common-session > etc/pam.d/common-session \  
&& sed \  
-e 's/\$session_nonint_primary/session [default=1] pam_permit.so/g' \  
-e 's/\$session_nonint_additional/session required pam_unix.so/g' \  
usr/share/pam/common-session-noninteractive > etc/pam.d/common-session-
noninteractive \  
&& echo 'LANG=C.UTF-8' > etc/default/locale \  
&& (echo '#!/bin/sh'; echo '/bin/vi $*') > usr/bin/sensible-editor \  
&& chmod +x usr/bin/sensible-editor \  
&& find \  
etc/security/*.conf \  
etc/selinux/*.conf \  
etc/*.conf \  
etc/crontab \  
etc/pam.d/* \  
etc/sudoers \  
| xargs -I % sed -i -r \  
-e 's,^[[:space:]]*[#]+.*$,,g' \  
-e 's,[[:space:]]+, ,g' \  
-e '/^[[:space:]]*$/d' \  
% \  
&& rm -rf \  
usr/share  
  
WORKDIR /  
  
  
FROM clover/busybox  
  
ENV LANG=C.UTF-8  
  
COPY --from=build /rootfs /  
  
ENTRYPOINT ["tini", "--"]  
  
CMD ["sh"]  

