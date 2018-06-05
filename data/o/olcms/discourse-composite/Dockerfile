FROM discourse/discourse:1.3.10  
LABEL maintainer "jacek@askesis.pl"  
  
RUN mkdir -p /discourse-composite/  
  
COPY build /discourse-composite/build  
  
RUN /discourse-composite/build/scripts/apply-templates.py \  
build/templates/web.template.yml build/templates/web.ratelimited.template.yml  
  
COPY run /discourse-composite/run  
  
VOLUME ["/var/www/discourse/public/", "/shared/", "/var/log"]  
  
ENTRYPOINT ["/discourse-composite/run/scripts/entrypoint.sh"]  
  

