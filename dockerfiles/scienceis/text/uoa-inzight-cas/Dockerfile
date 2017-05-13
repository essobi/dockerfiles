# ------------------------------
#
# Build for Census At School (CAS) 
# on top of the base CAS build
#
# ------------------------------
FROM scienceis/uoa-inzight-cas-base:latest

MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz

# Edit the following environment variable, commit to Github and it will trigger Docker build
# Since we fetch the latest changes from the associated Application~s master branch
# this helps trigger date based build
# The other option would be to tag git builds and refer to the latest tag
ENV LAST_BUILD_DATE="2016-03-11"
# install iNZight CAS Application
RUN rm -rf /srv/shiny-server/* \
  && wget -O CAS.zip https://github.com/iNZightVIT/CAS/archive/master.zip \
  && unzip CAS.zip \
  && rm -rf CAS.zip \
  && cp -R CAS-master/* /srv/shiny-server \
  && echo $LAST_BUILD_DATE > /srv/shiny-server/build.txt \
  && rm -rf CAS-master/ \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# handle DB config info separately
COPY config.R /srv/shiny-server/

# start shiny server process - it listens to port 3838
CMD ["/opt/shiny-server.sh"]
