FROM eiffel/develop:dev  
MAINTAINER Jocelyn Fiat  
LABEL description=" \  
IRON repository service. \  
To use it: \  
docker run -t -i eiffel/iron \  
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
USER root  
#RUN apt-get install -y apache2 libapache2-mod-fcgid libfcgi-dev  
#RUN a2enmod rewrite  
#RUN a2enmod suexec  
#RUN a2enmod include  
#RUN a2enmod fcgid  
#RUN service apache2 restart  
# Copy iron related scripts  
USER root  
COPY iron/ $EIF_IRON_DIR/  
RUN /bin/chown eiffel -R $EIF_IRON_DIR  
  
USER eiffel  
RUN /bin/chmod u+x $EIF_IRON_DIR/scripts/*.sh  
WORKDIR $EIF_IRON_DIR/scripts/  
  
RUN /bin/bash $EIF_IRON_DIR/scripts/iron_install.sh $EIF_IRON_DIR
$EIF_IRON_PORT "ironman" "eiffel123" \--clean  
  
# Entrypoint  
USER eiffel  
WORKDIR $EIF_IRON_DIR/www  
CMD $EIF_IRON_DIR/bin/irond  
  

