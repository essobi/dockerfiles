FROM errbit/errbit:latest  
  
LABEL \  
maintainer="Tobias L. Maier <me@tobiasmaier.info>" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.name="Errbit with Entrypoint script" \  
org.label-schema.vcs-url="https://github.com/tmaier/errbit-helm"  
  
USER root  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
USER errbit  
  
CMD ["puma","-C","config/puma.default.rb"]  
ENTRYPOINT ["docker-entrypoint.sh"]  

