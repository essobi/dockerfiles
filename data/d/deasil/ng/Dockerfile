FROM node:8.9  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL maintainer="Craig Johnston <cjimti@gmail.com>"  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Angular / NodeJS Development" \  
org.label-schema.description=" NodeJS / Angular CLI Development Container" \  
org.label-schema.url="https://deasil.works" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/deasilworks/docker-ng" \  
org.label-schema.vendor="Deasil Works Inc." \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
RUN useradd --user-group --create-home app  
  
# utils, dev libs and node  
RUN apt-get update \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
-y nodejs  
  
# node packages and gems  
RUN apt-get install -y ruby-full \  
&& curl -o- -L https://yarnpkg.com/install.sh | bash \  
&& gem install sass \  
&& /root/.yarn/bin/yarn global add @angular/cli  
  
ENV HOME=/home/app  
WORKDIR $HOME  
  
USER app  
  
EXPOSE 4200  

