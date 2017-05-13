FROM scienceis/uoa-catchit-common:latest

MAINTAINER ws@sit.auckland.ac.nz

# copy over the app folder with data samples
COPY app/* /srv/shiny-server/

COPY shiny-server.sh /usr/bin/shiny-server.sh

RUN chmod +x /usr/bin/shiny-server.sh

CMD ["/usr/bin/shiny-server.sh"]
