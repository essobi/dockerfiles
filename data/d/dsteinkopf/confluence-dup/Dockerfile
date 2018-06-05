FROM cptactionhank/atlassian-confluence  
  
# disable breadcumbs  
# see
https://confluence.atlassian.com/display/CONFKB/How+to+disable+hiding+(ellipsing)+of+breadcrumbs  
USER root  
RUN sed --in-place=.orig \  
's/#if ($ellipsisCrumbs.contains($breadcrumb))/#if (false)/' \  
"${CONF_INSTALL}/confluence/breadcrumbs.vm"  
  
USER daemon:daemon  
  

