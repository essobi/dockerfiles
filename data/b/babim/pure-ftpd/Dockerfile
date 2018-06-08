FROM babim/debianbase:ssh  
  
# properly setup debian sources  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://http.debian.net/debian jessie main\n\  
deb-src http://http.debian.net/debian jessie main\n\  
deb http://http.debian.net/debian jessie-updates main\n\  
deb-src http://http.debian.net/debian jessie-updates main\n\  
deb http://security.debian.org jessie/updates main\n\  
deb-src http://security.debian.org jessie/updates main\n\  
" > /etc/apt/sources.list  
RUN apt-get -y update  
  
# install package building helpers  
RUN apt-get -y --force-yes install dpkg-dev debhelper  
  
# install dependancies  
RUN apt-get -y build-dep pure-ftpd  
  
# build from source  
RUN mkdir /tmp/pure-ftpd/ && \  
cd /tmp/pure-ftpd/ && \  
apt-get source pure-ftpd && \  
cd pure-ftpd-* && \  
sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \  
dpkg-buildpackage -b -uc  
  
# install the new deb files  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb  
RUN apt-get -y install openbsd-inetd  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd_*.deb  
  
# Prevent pure-ftpd upgrading  
RUN apt-mark hold pure-ftpd pure-ftpd-common  
  
# setup ftpgroup and ftpuser  
RUN groupadd ftpgroup  
RUN useradd -g ftpgroup -d /home/ftpusers -s /dev/null ftpuser  
  
ENV PUBLICHOST ftp.foo.com  
  
VOLUME /home/ftpusers  
  
# Secure defaults, ref: https://github.com/stilliard/docker-pure-
ftpd/issues/10  
RUN cd /etc/pure-ftpd/conf/ && \  
echo "yes" | tee AntiWarez ChrootEveryone CreateHomeDir CustomerProof
Daemonize DontResolve IPV4Only NoAnonymous NoChmod NoRename
ProhibitDotFilesRead ProhibitDotFilesWrite \  
echo "no" | tee AllowAnonymousFXP AllowDotFiles AllowUserFXP
AnonymousCanCreateDirs AnonymousCantUpload AnonymousOnly AutoRename
BrokenClientsCompatibility CallUploadScript DisplayDotFiles IPV6Only
KeepAllFiles LogPID NATmode PAMAuthentication UnixAuthentication VerboseLog  
  
RUN mkdir /etc-start/ \  
&& mv /etc/pure-ftpd /etc-start && mkdir /etc/pure-ftpd  
  
# startup  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 21 22 30000-30009  

