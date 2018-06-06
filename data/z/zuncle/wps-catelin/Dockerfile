FROM zuncle/52n-wps  
MAINTAINER Pixime Consulting <xavier.thomas@pixime.fr>  
  
# 1. install gdal, unzip and openmpi  
RUN apt-get update -y \  
&& apt-get install gdal-bin python-gdal libgdal-dev unzip libopenmpi-dev
openmpi-bin -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# 2. install tauDEM  
WORKDIR /usr/src  
RUN wget https://github.com/dtarb/TauDEM/archive/Develop.zip  
  
RUN unzip Develop.zip \  
&& rm Develop.zip \  
&& cd TauDEM-Develop/src \  
&& export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/include/gdal \  
&& make  
  
ENV PATH /usr/src/TauDEM-Develop:$PATH  
  
# 3. Some tests  
RUN gdalinfo --version && gdalinfo --formats && ogrinfo --formats  
  
RUN mpiexec --version  
  
# 4. get Logan dem sample file  
RUN mkdir /tauDEM  
RUN mkdir /tauDEM/data  
RUN mkdir /tauDEM/debug  
  
WORKDIR /tauDEM/data  
RUN wget http://hydrology.usu.edu/taudem/taudem5/LoganDemo.zip \  
&& unzip LoganDemo.zip \  
&& rm LoganDemo.zip  
  
# 5. process Logan dem  
WORKDIR /tauDEM/data/Logan  
RUN mv logan.tif dem.tif  
RUN mpiexec -n 8 pitremove -z dem.tif -fel demfel.tif \  
&& mpiexec -n 8 d8flowdir -p demp.tif -sd8 demsd8.tif -fel demfel.tif \  
&& mpiexec -n 8 aread8 -p demp.tif -ad8 demad8.tif \  
&& mpiexec -n 8 threshold -ssa demad8.tif -src demsrc.tif -thresh 100 \  
&& ls  
  
# 6. clone and build wps-catelin repository  
WORKDIR /usr/src  
RUN git clone https://zuncle@bitbucket.org/zuncle/wps-catelin.git  
WORKDIR /usr/src/wps-catelin  
RUN mvn clean install -Dmaven.test.skip=true  
  
# 7. copy jar file to WEB-INF/lib  
RUN cp -R /usr/src/wps-catelin/target/pixime-wps-catelin-1.0.0-SNAPSHOT.jar
$CATALINA_HOME/webapps/wps/WEB-INF/lib  
  
# 8. copy updated wps_config_geotools.xml  
WORKDIR $CATALINA_HOME/webapps/wps/config  
RUN rm wps_config_geotools.xml  
ADD wps_config_geotools.xml wps_config_geotools.xml  
#RUN wget https://bitbucket.org/zuncle/wps-
catelin/src/42469945087b942abc8dfb8d41a36c450dbd41ef/docker/wps_config_geotools.xml  
WORKDIR /tauDEM/data  
  
VOLUME /tauDEM/data  
VOLUME /tauDEM/debug  
  
CMD ["catalina.sh", "run"]  

