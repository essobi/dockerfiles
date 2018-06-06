FROM ruby:2.4.1-alpine3.6  
ENV WORKPATH="/usr/src/app"  
RUN set -x \  
&& mkdir -p "${WORKPATH}" \  
&& apk add --no-cache git \  
&& gem install danger:5.4.1 \  
danger-todoist:1.2.3 \  
danger-lgtm:0.2.0 \  
danger-slack:0.0.3 \  
danger-commit_lint:0.0.6 \  
danger-rubocop:0.4.1  
  
WORKDIR ${WORKPATH}  
  
CMD ["danger"]  

