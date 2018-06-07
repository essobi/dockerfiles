# v1.5 2018-03-06 webmaster@highskillz.com  
#  
# Speed up moodle-based builds by pre-caching it in an image  
# It will be available for multi-image builds  
#  
FROM alpine:3.7 as base  
LABEL maintainer="webdev@highskillz.com"  
  
# ----------------------------------------------------------------  
FROM ez123/ops-base:alpine37 as downloads  
  
ARG MOODLE__VERSION=33  
ARG MOODLE__FETCH_MODE=git  
ARG SRC_ROOT=/tmp/repo  
  
COPY ./*.sh /tmp/  
RUN chmod -cR a+x /tmp/*.sh  
RUN \  
mkdir -p ${SRC_ROOT} &&\  
cd ${SRC_ROOT} &&\  
ls -la . &&\  
/tmp/fetch-moodle.sh ${MOODLE__VERSION} ${SRC_ROOT} ${MOODLE__FETCH_MODE} &&\  
ls -la /tmp/* &&\  
cat /tmp/repo/.chkver.env &&\  
echo "..."  
  
# ----------------------------------------------------------------  
FROM base as final  
COPY \--from=downloads /tmp/repo/moodle /tmp/moodle.bits/src  
COPY \--from=downloads /tmp/repo/.chkver.env /tmp/moodle.bits/  
  
ENTRYPOINT [exit]  

