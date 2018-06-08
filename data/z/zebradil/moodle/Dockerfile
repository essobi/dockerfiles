FROM zebradil/moodle  
  
LABEL maintainer="German Lashevich <german.lashevich@gmail.com>" \  
org.label-schema.schema-version="1.0.0-rc.1" \  
org.label-schema.name="zebradil/docker-moodle-coderunner" \  
org.label-schema.version="3.2-1" \  
org.label-schema.description="Lightweight Moodle container based on Alpine
Linux with preinstalled Coderunner plugin" \  
org.label-schema.vcs-url="https://github.com/Zebradil/docker-moodle.git"  
  
RUN cd /var/www/localhost/htdocs \  
&& git clone git://github.com/trampgeek/moodle-qtype_coderunner.git
question/type/coderunner \  
&& git clone git://github.com/trampgeek/moodle-
qbehaviour_adaptive_adapted_for_coderunner.git
question/behaviour/adaptive_adapted_for_coderunner  

