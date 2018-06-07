FROM mono:5  
MAINTAINER Andreas Fahrecker<fahrecker.a@gmail.com>  
  
ENV DMPUSER ksp-darkmultiplayer  
ENV DMPPATH /opt/darkmultiplayer  
ENV DMPV v0.2.4.4  
RUN apt-get -y update && \  
apt-get -y install unzip && \  
apt-get -y autoremove && \  
apt-get -y clean  
  
ADD https://d-mp.org/downloads/release/${DMPV}/DMPServer.zip /  
  
RUN unzip -j /DMPServer.zip -d $DMPPATH && \  
rm /DMPServer.zip  
  
ADD ./entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 6702  
RUN useradd $DMPUSER && \  
mkdir /data && \  
chown $DMPUSER:$DMPUSER /data && \  
chown $DMPUSER:$DMPUSER -R $DMPPATH  
VOLUME /data  
USER $DMPUSER  
CMD ./entrypoint.sh

