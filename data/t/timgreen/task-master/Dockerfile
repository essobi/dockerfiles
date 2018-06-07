ARG BASE=docker  
  
FROM ${BASE}  
MAINTAINER Tim Green "iamtimgreen@gmail.com"  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name='Task Master' \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url='https://github.com/timgreen/docker-task-master'  
  
RUN apk add --no-cache \  
bash \  
coreutils \  
git \  
openssh-client \  
curl \  
jq \  
python \  
py-pip \  
tmux \  
ncurses \  
inotify-tools \  
procps \  
&& pip install yq \  
&& pip install docker-compose \  
&& rm -fr ~/.cache/  
  
# papertrail  
ARG papertrail=true  
RUN if [[ $papertrail == true ]]; then \  
curl -L
https://github.com/papertrail/remote_syslog2/releases/download/v0.20-beta2/remote_syslog_linux_amd64.tar.gz
\  
-o remote_syslog.tar.gz \  
&& tar xzf remote_syslog.tar.gz \  
&& mv remote_syslog/remote_syslog /usr/bin/ \  
&& rm -fr remote_syslog remote_syslog.tar.gz \  
; \  
fi  
  
# graph-easy  
ARG graph_easy=true  
RUN if [[ $graph_easy == true ]]; then \  
apk add --no-cache perl perl-utils make \  
&& cpan -f Graph::Easy \  
&& rm -fr ~/.cpan/ \  
&& apk del perl-utils make \  
; \  
fi  
  
ADD entry-point.sh /entry-point.sh  
ADD status-manager.sh /status-manager.sh  
RUN chmod a+rx /entry-point.sh /status-manager.sh \  
&& ln -s /entry-point.sh /usr/bin/s  
  
ADD .terminfo/ /root/.terminfo  
ADD .tmux.conf /root/.tmux.conf  
  
ENV WORKDIR /dev/shm/  
  
ENTRYPOINT ["/entry-point.sh"]  
CMD ["daemon"]  

