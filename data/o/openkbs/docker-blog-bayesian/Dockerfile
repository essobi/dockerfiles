FROM openkbs/jdk-mvn-py3-x11  
#FROM openkbs/atom-java-mvn-python3  
  
MAINTAINER DrSnowbird "DrSnowbird@openkbs.org"  
  
ARG INSTALL_DIR=${INSTALL_DIR:-/opt}  
  
ARG TARGET_VER=${TARGET_VER:-0.10}  
  
ARG TARGET_TGZ=${TARGET_TGZ:-blog-${TARGET_VER}.zip}  
ARG
TARGET_URL=${TARGET_URL:-https://bayesianlogic.github.io/download/${TARGET_TGZ}}  
  
ARG TARGET_HOME=${TARGET_HOME:-${INSTALL_DIR}/blog-${TARGET_VER}}  
ENV TARGET_HOME=${TARGET_HOME}  
  
ARG TARGET_EXE=${TARGET_HOME}/bin/blog  
  
#############################  
#### ---- Install Target ----  
#############################  
WORKDIR ${INSTALL_DIR}  
  
RUN wget -c ${TARGET_URL} && \  
unzip ${TARGET_TGZ} && \  
rm ${TARGET_TGZ}  
  
RUN ln -s ${TARGET_EXE} /usr/bin/$(basename ${TARGET_EXE}) && \  
ls -al ${TARGET_HOME} && \  
mkdir -p /workspace  
  
#############################  
#### ---- Install Sublime ----  
#############################  
  
WORKDIR ${INSTALL_DIR}  
  
ARG
SUBLIME_URL=${SUBLIME_URL:-https://download.sublimetext.com/sublime_text_3_build_3143_x64.tar.bz2}  
ARG SUBLIME_VER=${SUBLIME_VER:-build_3143_x64}  
ARG SUBLIME_DIR=${SUBLIME_DIR:-sublime_text_3}  
  
RUN wget -c ${SUBLIME_URL} && \  
tar -vxjf ${SUBLIME_DIR}_${SUBLIME_VER}.tar.bz2 && \  
rm ${SUBLIME_DIR}_${SUBLIME_VER}.tar.bz2  
  
RUN ln -s ${INSTALL_DIR}/${SUBLIME_DIR}/sublime_text /usr/bin/sublime_text &&
\  
ls -al ${TARGET_HOME} && \  
mkdir -p ${HOME}/.config/sublime-text-3/Packages/User ${HOME}/data
${HOME}/workspace && \  
ls -al ${HOME}/.config  
  
COPY editors/blog-for-sublime/blog* ${HOME}/.config/sublime-
text-3/Packages/User/  
RUN /bin/chown -R ${USER_ID}:${USER_ID} ${HOME}/.config ${HOME}/data
${HOME}/workspace && \  
ls -al ${HOME}/.config/sublime-text-3/Packages/User/ && \  
find ${HOME}/.config  
  
  
#############################  
#### ---- Workspace setup ----  
#############################  
USER "developer"  
  
VOLUME "${HOME}/data"  
VOLUME "${HOME}/workspace"  
VOLUME "${HOME}/.config"  
  
WORKDIR /workspace  
  
ENV TARGET_EXE=${TARGET_EXE}  
  
#ENTRYPOINT "${TARGET_EXE}" "${TARGET_HOME}/example/burglary.blog"  
  
#RUN echo $HOME  
CMD "/usr/bin/sublime_text" "${TARGET_HOME}/example/burglary.blog"  

