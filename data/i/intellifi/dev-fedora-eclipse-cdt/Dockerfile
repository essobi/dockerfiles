FROM intellifi/dev-fedora-base  
  
MAINTAINER Intellifi https://intellifi.nl  
LABEL version="2.1.0" \  
description="Intellifi development environment container for Eclipse CDT"  
  
RUN dnf install -y --best --allowerasing eclipse-cdt \  
&& dnf clean all \  
&& useradd --create-home --user-group builder  
  
USER builder  
  
RUN \  
eclipse --launcher.suppressErrors -nosplash -application
org.eclipse.equinox.p2.director -repository "http://gnu-mcu-
eclipse.netlify.com/v4-neon-updates" -installIU ilg.gnumcueclipse.core \  
&& eclipse --launcher.suppressErrors -nosplash -application
org.eclipse.equinox.p2.director -repository "http://gnu-mcu-
eclipse.netlify.com/v4-neon-updates" -installIU
ilg.gnumcueclipse.managedbuild.cross \  
&& eclipse --launcher.suppressErrors -nosplash -application
org.eclipse.equinox.p2.director -repository "http://gnu-mcu-
eclipse.netlify.com/v4-neon-updates" -installIU
ilg.gnumcueclipse.managedbuild.cross.arm  

