FROM debian:testing  
RUN apt-get update && apt-get -y install git planet-venus xsltproc  
RUN git clone https://github.com/rozie/PlanetJogger.git  
RUN sed -e 's@/home/rozie/planetjogger/index.html.tmpl #
CHANGEME@/PlanetJogger/index.html.tmpl@' -i PlanetJogger/planet-jogger.ini  
RUN sed -e 's@output_dir.*@output_dir = /var/www/planetjogger@' -i
PlanetJogger/planet-jogger.ini  
RUN cd PlanetJogger && planet planet-jogger.ini  

