FROM elasticsearch:2  
  
MAINTAINER Fernando Moro <fernando.moro@radmas.com>  
  
LABEL org.mejoratuciudad.vendor="Radmas Technologies"  
LABEL org.mejoratuciudad.image-name="mtc-plus-elasticsearch"  
LABEL version="1.0"  
LABEL description="Search engine."  
  
#################################################  
# ELASTICSEARCH  
  
RUN /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head  
  
CMD ["elasticsearch", "--default.path.repo=/backups"]  

