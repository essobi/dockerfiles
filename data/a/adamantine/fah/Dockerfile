FROM debian  
  
ENV USERNAME workernode  
ENV TEAM 233907  
ENV POWER medium  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl bzip2 \  
&& curl -O
http://folding.stanford.edu/releases/public/release/fahclient/debian-
testing-64bit/v7.4/latest.deb \  
&& dpkg -i latest.deb \  
&& chown fahclient:root /etc/fahclient/config.xml \  
&& sed -i -e "s/<team value=\"0\"\/>/<team value=\""$TEAM"\"\/>/;s/<user
value=\"Anonymous\"\/>/<user value=\""$USERNAME"\"\/>/;s/<power
value=\"medium\"\/>/<power value=\""$POWER"\"\/>/" /etc/fahclient/config.xml \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get purge --remove curl -y  
  
CMD FAHClient --config /etc/fahclient/config.xml  

