FROM dclong/r-pop  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends wget \  
&& rstudio_version=$(wget --no-check-certificate -qO-
https://s3.amazonaws.com/rstudio-server/current.ver) \  
&& wget https://download2.rstudio.org/rstudio-
server-${rstudio_version}-amd64.deb -O /rstudio-server.deb \  
&& apt-get install -y --no-install-recommends /rstudio-server.deb \  
&& rm /rstudio-server.deb  
  
EXPOSE 8787  
ADD settings/Rprofile.site /usr/local/lib/R/etc/  
# ADD userconf.sh /etc/cont-init.d/conf  
# ADD rstudio /etc/services.d/  
ADD scripts/launch.sh /scripts/  
  
ENTRYPOINT ["/scripts/init.sh"]  
  

