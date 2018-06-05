# Galaxy - NeuroLINCS Edition  
#  
# VERSION 0.4  
FROM quay.io/bgruening/galaxy:17.09  
MAINTAINER Alex LeNail "alex@lenail.org"  
ENV GALAXY_CONFIG_BRAND="AnswerALS" \  
  
GALAXY_CONFIG_ERROR_EMAIL_TO="alex@lenail.org" \  
GALAXY_CONFIG_EMAIL_FROM="alex@lenail.org" \  
  
GALAXY_CONFIG_USER_ACTIVATION_ON="False" \  
GALAXY_CONFIG_ACTIVATION_GRACE_PERIOD="0" \  
GALAXY_CONFIG_INACTIVITY_BOX_CONTENT="Your account has not been activated yet.
Feel free to browse around and see what's available, but you won't be able to
upload data or run jobs until you have verified your email address." \  
GALAXY_CONFIG_REQUIRE_LOGIN="True" \  
GALAXY_CONFIG_SHOW_WELCOME_WITH_LOGIN="True" \  
GALAXY_CONFIG_EXPOSE_USER_NAME="True" \  
GALAXY_CONFIG_EXPOSE_USER_EMAIL="True" \  
GALAXY_CONFIG_ALLOW_USER_CREATION="False" \  
GALAXY_CONFIG_ALLOW_USER_DELETION="True" \  
GALAXY_CONFIG_ALLOW_USER_IMPERSONATION="True" \  
GALAXY_CONFIG_ALLOW_USER_DATASET_PURGE="True" \  
GALAXY_CONFIG_ALLOW_LIBRARY_PATH_PASTE="True" \  
GALAXY_CONFIG_NEW_USER_DATASET_ACCESS_ROLE_DEFAULT_PRIVATE="True" \  
  
GALAXY_CONFIG_USE_NGLIMS="False" \  
GALAXY_CONFIG_NGLIMS_CONFIG_FILE="tool-data/nglims.yaml" \  
  
GALAXY_CONFIG_ENABLE_BETA_TOOL_COMMAND_ISOLATION="True" \  
GALAXY_CONFIG_SERVE_XSS_VULNERABLE_MIMETYPES="True" \  
  
GALAXY_CONFIG_USE_INTERACTIVE="False" \  
  
GALAXY_CONFIG_CONDA_AUTO_INSTALL="True" \  
GALAXY_CONFIG_CONDA_AUTO_INIT="True" \  
  
EXPORT_DIR_PREFIX="/pool/data/globus/"  
# GALAXY_HANDLER_NUMPROCS=2 \ # Set the number of Galaxy handlers -> we may
want to change this later.  
ENV TERM=xterm  
  
RUN add-tool-shed --url 'https://testtoolshed.g2.bx.psu.edu/' \--name 'Test
Tool Shed'  
  
# Install tools  
ADD ./tools.yml $GALAXY_ROOT/tools.yml  
RUN install-tools $GALAXY_ROOT/tools.yml  
  
# Add Workflows  
RUN mkdir -p $GALAXY_HOME/workflows  
ADD ./workflows/* $GALAXY_HOME/workflows/  
  
RUN startup_lite && \  
galaxy-wait && \  
workflow-install --workflow_path $GALAXY_HOME/workflows/ -g
http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p
$GALAXY_DEFAULT_ADMIN_PASSWORD  
  
# Configure Galaxy Homepage  
ADD ./welcome.html $GALAXY_CONFIG_DIR/web/welcome.html  
ADD ./welcome_banner.png $GALAXY_CONFIG_DIR/web/welcome_banner.png  
  
# Mark folders as imported from the host.  
VOLUME ["/export/", "/data/", "/var/lib/docker"]  
  
# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9002 (supervisor
webui)  
EXPOSE :80  
EXPOSE :21  
EXPOSE :22  
EXPOSE :8800  
EXPOSE :9002  
# Expose ports for in-galaxy globus  
# EXPOSE :2811  
# EXPOSE :2223  
# EXPOSE :7512  
# EXPOSE :50000-51000  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]  
  

