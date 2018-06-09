FROM rocker/geospatial:3.4.1  
# Earth Engine  
RUN apt-get -y install python-pip \  
&& pip install google-api-python-client \  
&& pip install earthengine-api \  
&& pip install pyasn1 --upgrade \  
&& apt-get -y install python-pandas  
  
# Hugo  
RUN cd ~ \  
&& wget
https://github.com/spf13/hugo/releases/download/v0.20.7/hugo_0.20.7_Linux-64bit.deb
\  
&& dpkg -i hugo*.deb \  
&& rm hugo*.deb  
  
# JAGS  
RUN wget http://ftp.debian.org/debian/pool/main/j/jags/jags_4.3.0.orig.tar.gz
-P /usr/local \  
&& tar xvzf /usr/local/jags_4.3.0.orig.tar.gz -C /usr/local/bin \  
&& rm /usr/local/jags_4.3.0.orig.tar.gz \  
&& cd /usr/local/bin/JAGS-4.3.0 \  
&& ./configure \  
&& make \  
&& make install  
  
# Additional R packages  
RUN R -e "devtools::install_github('lme4/lme4', dependencies=TRUE)" \  
&& R -e "devtools::install_github('jrnold/ggthemes')" \  
&& R -e "devtools::install_github('yixuan/showtext')" \  
&& R -e "devtools::install_github('jeremystan/tidyjson')" \  
&& R -e "devtools::install_github('rstudio/blogdown')" \  
&& R -e "devtools::install_github('adletaw/captioner')" \  
&& R -e "devtools::install_github('haozhu233/kableExtra',
ref='f200ce56bafab4dcfaaada294cd9d1b9599d2c68')" \  
&& R -e "devtools::install_github('rstudio/leaflet')" \  
&& R -e "devtools::install_github('bhaskarvk/leaflet.extras')" \  
&& R -e "install.packages('rjags', configure.args='--with-jags-
include=/usr/local/include/JAGS --with-jags-lib=/usr/local/lib/JAGS --with-
jags-modules=/usr/local/lib/JAGS/modules')"  

