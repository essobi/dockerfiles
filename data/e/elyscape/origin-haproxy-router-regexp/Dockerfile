FROM openshift/origin-haproxy-router  
  
# The template file is now owned by root with file mode 0644, so we have  
# to switch back to root in order to modify it.  
USER 0  
  
# First line switches to regular expression matching on map files with paths  
# Second line locks map files with paths to match the beginning of the URI  
RUN sed -i \  
-e '/os_\\(reencrypt\|http_be\|edge_http_\\(redirect\|be\|expose\\)\\)\\.map/ s/map_beg/map_reg/' \  
-e 's/^{{$cfg.Host}}{{$cfg.Path}}/^&/' \  
/var/lib/haproxy/conf/haproxy-config.template  
  
USER 1001  

