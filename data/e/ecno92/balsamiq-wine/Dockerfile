# A docker container to run the balsamiq mockup tool with the help of wine.  
# Please make sure that you fill in the LICENSE environment variables when
launching the app.  
#  
# docker run --rm -it \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -e BALSAMIC_LICENSENAME="" \  
# -e BALSAMIC_LICENSEKEY="" \  
# -e USERPERMS="$(stat -c '%u:%g' $(pwd))" \  
# -v "$(pwd)":/home/balsamiq/shared-data \  
# -u balsamiq \  
# --name balsamiq \  
# ecno92/balsamiq-wine  
#  
FROM r.j3ss.co/wine  
MAINTAINER Therry van Neerven <mail@therryvanneerven.nl>  
  
ADD https://builds.balsamiq.com/mockups-
desktop/Balsamiq_Mockups_3.5.7_bundled.zip /usr/src/Balsamiq_Mockups.zip  
  
RUN apt-get update && apt-get install -y unzip && \  
unzip /usr/src/Balsamiq_Mockups.zip -d /opt > /dev/null && \  
apt-get remove -y unzip && rm -rf /var/lib/apt/lists/*  
  
ENV HOME /home/balsamiq  
RUN useradd --create-home --home-dir $HOME balsamiq  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

