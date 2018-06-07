FROM java:jre  
MAINTAINER "Nathaniel Rankin Webb" <nrwebb@live.com>  
  
ENV HOME /opt/jetbrains/upsource  
ENV VERSION 2.5  
ENV BUILD ${VERSION}.5074  
ENV ZIP upsource-${BUILD}.zip  
  
RUN printf "* - memlock unlimited\n" >> \  
printf "* - nofile 100000\n" >> \  
printf "* - nproc 32768\n" >> \  
printf "* - as unlimited" >> /etc/security/limits.conf  
  
WORKDIR $HOME  
RUN wget --progress bar:force:noscroll
https://download.jetbrains.com/upsource/$ZIP && \  
unzip -q $ZIP -d . && \  
rm $ZIP && \  
mv Upsource/* $HOME && \  
rmdir Upsource  
  
VOLUME ["$HOME"]  
EXPOSE 8080  
ENTRYPOINT ["bin/upsource.sh"]  
CMD ["run"]  

