# CoMSES miracle docker image for radiant and shiny server  
# Mount Points  
# /var/log/shiny-server.log log file  
# /miracle/projects project files  
  
FROM comses/miracle-r  
  
ENV PROJECTS_PATH /miracle/projects  
ENV USERNAME comses  
ARG SHINY_SERVER_VERSION=1.4.4.807  
ARG SHINY_RPM=shiny-server-$SHINY_SERVER_VERSION-rh5-x86_64.rpm  
ARG MIRACLE_RADIANT_URL=https://github.com/warmdev/radiant-mod.git  
ARG SHINY_INSTALL_DIR=/srv/shiny-server  
  
USER root  
WORKDIR /opt/  
  
# Install Shiny Server  
RUN wget -q https://download3.rstudio.org/centos5.9/x86_64/$SHINY_RPM \  
&& yum install -y --nogpgcheck $SHINY_RPM && rm -f $SHINY_RPM \  
# Install Radiant  
&& git clone \--depth 1 $MIRACLE_RADIANT_URL $SHINY_INSTALL_DIR/radiant \  
&& cp -r $SHINY_INSTALL_DIR/radiant/inst/* $SHINY_INSTALL_DIR \  
&& cp -r $SHINY_INSTALL_DIR/radiant/R /srv \  
&& rm -rf $SHINY_INSTALL_DIR/radiant \  
# Configure Shiny and Radiant  
# ---------------------------  
&& sed -i -e "s/run_as shiny/run_as $USERNAME/g" /etc/shiny-server/shiny-
server.conf \  
&& mkdir -p $PROJECTS_PATH \  
&& ln -s $PROJECTS_PATH $SHINY_INSTALL_DIR/miracle \  
&& chown -R $USERNAME: $PROJECTS_PATH $SHINY_INSTALL_DIR \  
# Create a log file  
&& mkdir -p /var/log/shiny-server \  
&& touch /var/log/shiny-server.log \  
&& chown -R $USERNAME: /var/log/shiny-server* \  
&& R -e
"devtools::install_url('https://cran.r-project.org/src/contrib/Archive/shiny/shiny_0.13.2.tar.gz')"
\  
&& yum clean all  
  
USER $USERNAME  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server"]  

