FROM clojure:lein-2.7.1-alpine AS reporter-builder  
  
COPY qualified/codewars-reporter /tmp/codewars-reporter  
WORKDIR /tmp/codewars-reporter  
RUN mv "$(lein uberjar | sed -n 's/^Created \\(.*standalone\\.jar\\)/\1/p')"
codewars-reporter.jar  
  
FROM clojure:lein-2.7.1-alpine  
# derived from openjdk:8-alpine  
# `leiningen-2.7.1-standalone.jar` has Clojure 1.8.0  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
COPY \--from=reporter-builder \  
/tmp/codewars-reporter/codewars-reporter.jar \  
/runner/codewars-reporter.jar  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

