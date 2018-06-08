FROM skopciewski/ruby  
  
RUN apk add \--no-cache git \  
&& apk-install-build-dependencies  
RUN gem-install pry  
RUN bundle config build.nokogiri --use-system-libraries  
  
ENV BUNDLE_WITHOUT=""  
ENV PROJECT_DIR=/opt/project/code  
ENV user=project  
ARG uid=1000  
ARG gid=1000  
  
RUN mkdir -p ${PROJECT_DIR} \  
&& addgroup -g ${gid} ${user} \  
&& adduser -h /home/${user} -D -u ${uid} -G ${user} -s /bin/sh ${user} \  
&& cp /root/.gemrc /home/${user}/.gemrc \  
&& cp -r /root/.bundle /home/${user}/.bundle \  
&& mkdir ${BUNDLE_APP_CONFIG} \  
&& touch ${BUNDLE_APP_CONFIG}/config \  
&& chown -R ${user}:${user} ${GEM_HOME} ${PROJECT_DIR} /home/${user}/.gemrc \  
/home/${user}/.bundle ${BUNDLE_APP_CONFIG}/config  
  
USER ${user}  
  
WORKDIR ${PROJECT_DIR}  

