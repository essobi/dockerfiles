FROM gshipley/javabase:latest  
MAINTAINER Grant Shipley, https://github.com/gshipley  
  
  
# Rev-locking this to ensure reproducible builds  
RUN wget -O /tmp/runas.sh 'https://raw.githubusercontent.com/coppit/docker-
inotify-command/master/runas.sh'  
RUN wget -O /tmp/mapids.sh 'https://raw.githubusercontent.com/coppit/docker-
inotify-command/master/50_remap_ids.sh'  
RUN chmod +x /tmp/runas.sh  
RUN chmod +x /tmp/mapids.sh  
  
# Run as root by default  
ENV USER_ID 0  
ENV GROUP_ID 0  
ENV UMASK 0000  
ENV UMAP ""  
ENV GMAP ""  
RUN curl http://www.blisshq.com/app/latest-linux-version|xargs wget -O
/tmp/latest.jar  
  
RUN echo INSTALL_PATH=/bliss > /tmp/auto-install.properties  
RUN java -jar /tmp/latest.jar -options /tmp/auto-install.properties  
RUN ln -s /config /root/.bliss  
RUN chmod +777 /bliss  
CMD /tmp/runas.sh $USER_ID $GROUP_ID $UMASK /bliss/bin/bliss.sh  
  
VOLUME /config /music  
  
EXPOSE 3220 3221  

