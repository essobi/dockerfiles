FROM jayess/tempus-base  
  
USER root  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qy install gdb  
RUN /venv/bin/pip install --upgrade --no-cache-dir \  
https://github.com/jsza/getoverhere/zipball/master  
  
USER steam  
ENV HOME /home/steam  
ENV STEAMCMD $HOME/steamcmd  
  
COPY ./update_tf2.txt $STEAMCMD/update_tf2.txt  
COPY ./run_tf2.sh $STEAMCMD/run_tf2.sh  
COPY ./update_tempus.py /srv/update_tempus.py  
  
RUN $STEAMCMD/steamcmd.sh +quit  
  
USER root  
  
# SRCDS is the nicest  
ENTRYPOINT ["/usr/bin/nice", "-n", "-20", \  
"/usr/bin/sudo", "--user", "steam", "/home/steam/steamcmd/run_tf2.sh"]  

