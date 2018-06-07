FROM debian:jessie  
  
RUN dpkg --add-architecture i386  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qy install --no-
install-recommends python python-pip ca-certificates git libpq5:i386
libgcc1:i386 libtinfo5:i386 libncurses5:i386 wget build-essential libffi-dev
python-dev libssl-dev zip  
RUN pip install virtualenv \  
&& python -m virtualenv /venv \  
&& /venv/bin/pip install --no-cache-dir \  
https://github.com/jsza/getoverhere/zipball/master \  
&& /venv/bin/pip install --upgrade --no-cache-dir \  
https://github.com/jsza/getoverhere/zipball/master  
RUN adduser --uid 5000 --disabled-password --gecos "" steam  
  
USER steam  
ENV HOME /home/steam  
ENV STEAMCMD $HOME/steamcmd  
  
RUN mkdir $STEAMCMD && wget -O -
http://media.steampowered.com/client/steamcmd_linux.tar.gz | tar -C $STEAMCMD
-xvz  
  
COPY ./update_css.txt $STEAMCMD/update_css.txt  
COPY ./run_css.sh $STEAMCMD/run_css.sh  
  
RUN $STEAMCMD/steamcmd.sh +quit  
  
ENTRYPOINT ["/home/steam/steamcmd/run_css.sh"]  

