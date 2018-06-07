FROM base/archlinux  
  
RUN echo -e "[oracle]\nSigLevel = Optional TrustAll\nServer =
http://linux.shikadi.net/arch/\$repo/\$arch/" >>/etc/pacman.conf  
  
RUN pacman --sync --refresh --noconfirm --noprogressbar --quiet && pacman
--sync --noconfirm --noprogressbar --quiet oracle-sqldeveloper libxrender
libxtst libcups fontconfig ttf-dejavu  
  
RUN echo 'AddVMOption -Dide.user.dir=/data' >> /opt/oracle-
sqldeveloper/sqldeveloper/bin/sqldeveloper.conf  
  
VOLUME /data  
WORKDIR /data  
  
ENV ORACLE_HOME /usr  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk  
  
CMD oracle-sqldeveloper  

