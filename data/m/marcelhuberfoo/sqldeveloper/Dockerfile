FROM marcelhuberfoo/arch  
  
USER root  
  
RUN echo -e "[oracle]\nSigLevel = Optional TrustAll\nServer =
http://linux.shikadi.net/arch/\$repo/\$arch/" >>/etc/pacman.conf  
  
RUN pacman -Syy --noconfirm reflector && \  
reflector --latest 5 --sort rate --save /etc/pacman.d/mirrorlist  
RUN pacman -Syyu --noconfirm && \  
pacman-db-upgrade && \  
pacman -S --noconfirm oracle-sqldeveloper libxrender libxtst libcups
fontconfig ttf-dejavu && \  
printf "y\\\ny\\\n" | pacman -Scc  
  
RUN echo 'AddVMOption -Dide.user.dir=/data' >> /opt/oracle-
sqldeveloper/sqldeveloper/bin/sqldeveloper.conf  
  
RUN mkdir -p /data && chown -R $UID:$GID /data  
VOLUME ["/data"]  
WORKDIR /data  
  
ENV ORACLE_HOME=/usr JAVA_HOME=/usr/lib/jvm/java-7-openjdk  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["oracle-sqldeveloper"]  

