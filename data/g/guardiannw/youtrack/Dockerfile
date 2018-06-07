FROM java:jre  
MAINTAINER "Nathaniel Rankin Webb" <nrwebb@live.com>  
  
ENV HOME /opt/jetbrains/youtrack  
ENV VERSION 6.5  
ENV BUILD ${VERSION}.17057  
ENV ZIP youtrack-${BUILD}.zip  
  
WORKDIR $HOME  
RUN wget --progress bar:force:noscroll
https://download.jetbrains.com/charisma/$ZIP && \  
unzip $ZIP -d . && \  
rm $ZIP  
  
VOLUME ["$HOME"]  
EXPOSE 8080  
ENTRYPOINT ["bin/youtrack.sh"]  
CMD ["run"]  

