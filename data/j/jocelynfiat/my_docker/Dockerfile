#Usage : docker run -i -t -e "DISPLAY=192.168.1.4:0" jocelyn/eiffel-dev:iron-
dev  
FROM eiffel/devenv:trunk  
MAINTAINER Jocelyn Fiat  
LABEL description="Dev environment for IRON project.\  
To use it: \  
docker run -t -i eiffel/devenv:iron-dev \  
open a browser on http://localhost:9090/ \  
Iron default credential= ironman:eiffel123 \  
\  
The linux account is eiffel:eiffel \  
\  
To open an xterm, add the following argument \  
-e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix \  
and append "xterm" to the docker command line. \  
."  
  
USER eiffel  
ENV HOME /home/eiffel  
ENV EIF_IRON_DIR $HOME/iron  
ENV EIF_IRON_PORT 9090  
EXPOSE 9090  
#USER root  
#RUN apt-get install -y apache2 libapache2-mod-fcgid libfcgi-dev  
#RUN a2enmod rewrite  
#RUN a2enmod suexec  
#RUN a2enmod include  
#RUN a2enmod fcgid  
#RUN service apache2 restart  
#RUN apt-get install -y vim tmux  
# Copy iron related scripts  
USER root  
COPY iron/ $EIF_IRON_DIR/  
RUN /bin/chown eiffel -R $EIF_IRON_DIR  
  
USER eiffel  
RUN /bin/chmod u+x $EIF_IRON_DIR/scripts/*.sh  
RUN /bin/chmod u+x $EIF_IRON_DIR/scripts/upload/*upload_version.py  
WORKDIR $EIF_IRON_DIR/scripts/  
  
RUN ./iron_prepare.sh $EIF_IRON_DIR \--clean  
RUN ./iron_init.sh $EIF_IRON_DIR $EIF_IRON_PORT "ironman" "eiffel123"  
RUN ./iron_fill_trunk.sh $EIF_IRON_DIR $EIF_IRON_PORT "ironman" "eiffel123"  
  
# Entrypoint  
USER eiffel  
WORKDIR $EIF_IRON_DIR/www  
CMD $EIF_IRON_DIR/bin/irond  
  

