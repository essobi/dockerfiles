FROM cismet/cids-distribution-cache:5.0  
  
MAINTAINER Pascal Dihé <pascal.dihe@cismet.de>  
  
LABEL de.cismet.cids.distribution.switchon.name="cids-distribution-switchon
image" \  
de.cismet.cids.distribution.switchon.version="5.0-SNAPSHOT" \  
de.cismet.cids.distribution.switchon.tag.docker="5.0-SNAPSHOT" \  
de.cismet.cids.distribution.switchon.tag.git="cidsDistributionSwitchon-5.0-SNAPSHOT"
\  
de.cismet.cids.distribution.switchon.descripton="cids SWITCH-ON Distribution
Runtime Image"  
  
ENV CIDS_ACCOUNT_EXTENSION Switchon  
ENV CIDS_CODEBASE http://switchon-docker.cismet.de  
ENV CIDS_LOCAL_DIR ${CIDS_LIB_DIR}/local${CIDS_ACCOUNT_EXTENSION}  
ENV CIDS_STARTER_DIR ${CIDS_LIB_DIR}/starter${CIDS_ACCOUNT_EXTENSION}  
ENV UPDATE_SNAPSHOTS -U -Dmaven.clean.failOnError=false  
  
# The current switchon autodistribution creates a subdirectory for the client
JNLPs.  
# This is cids-distribution specific setting:  
# flatClientDirectory in switchon-navigator-distribution is set to FALSE!  
# NOTE: Client dir is created by cids-maven-plugin and is case sensitive!  
# ENV CIDS_CLIENT_DIR ${CIDS_DISTRIBUTION_DIR}/client/Switchon  
  
# expose cids-server port  
EXPOSE 9986  
  
# expose cids-server-rest port  
EXPOSE 8890  
  
# expose ngnix port  
EXPOSE 80  
  
# use .dockerignore to control which files go into the image and which not
(faster!)  
# cache is used if settings.xml & POM.xml do not change  
# lib/m2 is excluded by default -> use baseimage 'cids-distribution-cache'
instead!  
COPY cidsDistribution/ ${CIDS_DISTRIBUTION_DIR}/  
  
# download the cids-distribution-switchon SNAPSHOT or RELEASE auto
distribution  
# RUN curl -fsSL https://codeload.github.com/switchonproject/cids-
distribution-switchon/tar.gz/v5.1 | tar -xzC ${CIDS_GENERATOR_DIR}/  
  
# USE docker ADD instead of RUN for SNPASHOT Builds to omit the cache and
always download the latest DEV archive!  
ADD https://codeload.github.com/switchonproject/cids-distribution-
switchon/tar.gz/dev /tmp/dev.tar.gz  
RUN tar -xzf /tmp/dev.tar.gz -C ${CIDS_GENERATOR_DIR}/  
  
# prepare dowloads all dependencies and uses the build cache  
# this image inherits from cids-distribution-cache, so dependencies should be
there already  
# RUN ${CIDS_DISTRIBUTION_DIR}/utils/prepare_autodistribution.sh  
  
# unfortunately, prepare_autodistribution.sh does not download all required
plugins!  
# perform primimg build instead  
RUN ${CIDS_DISTRIBUTION_DIR}/utils/build_autodistribution.sh  
  
# clever signing of 'static' dependencies  
# DISABLED: now handled by auto-distribution v5 maven exec!  
# RUN ${CIDS_DISTRIBUTION_DIR}/utils/sign_all.sh  
  
# enable debug logging during mvn build (optional, disabled by default)  
#RUN sed -i \--
"s/org.slf4j.simpleLogger.defaultLogLevel=info/org.slf4j.simpleLogger.defaultLogLevel=debug/g"
${MAVEN_HOME}/conf/logging/simplelogger.properties \  
# && sed -i \--
"s/org.slf4j.simpleLogger.logFile=System.out/org.slf4j.simpleLogger.logFile=build.log/g"
${MAVEN_HOME}/conf/logging/simplelogger.properties  
  
# selectively invalidate build cache *after* this instruction if
'expire_after' build arg is provided (see build.sh)  
ARG expire_after=never  
  
# build the autodistribution using the *cached* and signed dependencies
downloaded in prepare_autodistribution.sh step  
# update snapshots and spossibly add new unsigned dependencies to lib/m2  
RUN ${CIDS_DISTRIBUTION_DIR}/utils/build_autodistribution.sh  
  
# force signing of *new* snapshot dependencies  
# DISABLED: now handled by auto-distribution v5 maven exec!  
# RUN ${CIDS_DISTRIBUTION_DIR}/utils/sign_all.sh  
  
# copy generated client jnlp to lib/start dir and generate security.jar->
required since host mounted  
# volume overlays client directory (default target for client JNLPs generated
by cids-java-maven plugin)  
# This behaviour is currently inconsistent with cids auto distribution (cids-
maven-plugin v5.0).  
# See https://github.com/cismet/cids-docker-images/issues/15  
RUN ${CIDS_DISTRIBUTION_DIR}/utils/copy_client_starter.sh  
  
# WARNING: private data is still present in intermediate image layers! Don't
push the image to public registries!  
# See https://github.com/docker/docker/issues/13490  
RUN rm -rf ${CIDS_DISTRIBUTION_DIR}/.private; exit 0  
RUN rm -rf ${CIDS_GENERATOR_DIR}; exit 0  
  
# add /tmp as volume since it may contain data that changes often  
VOLUME /tmp  

