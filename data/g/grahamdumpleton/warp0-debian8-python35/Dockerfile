FROM grahamdumpleton/warp0-debian8-base  
  
MAINTAINER Graham Dumpleton <Graham.Dumpleton@gmail.com>  
  
ENV WARPDRIVE_VERSION=0.27.0 \  
PYTHON_VERSION=3.5.3 \  
MOD_WSGI_VERSION=4.5.14  
ENV WARPDRIVE_APP_ROOT=/opt/app-root \  
WARPDRIVE_SRC_ROOT=/opt/app-root/src \  
WARPDRIVE_S2I_ROOT=/opt/app-root/s2i  
  
ENV PYTHONIOENCODING=UTF-8 \  
PYTHONUNBUFFERED=1  
RUN mkdir -p ${WARPDRIVE_APP_ROOT} \  
&& curl -SL -o /tmp/warpdrive.tar.gz
https://codeload.github.com/GrahamDumpleton/warpdrive/tar.gz/$WARPDRIVE_VERSION
\  
&& tar -xC ${WARPDRIVE_APP_ROOT} \--strip-components=1 -f
/tmp/warpdrive.tar.gz warpdrive-$WARPDRIVE_VERSION/warpdrive
warpdrive-$WARPDRIVE_VERSION/s2i \  
&& rm -f /tmp/warpdrive.tar.gz  
  
ENV PATH=${WARPDRIVE_APP_ROOT}/warpdrive/bin:$PATH  
  
RUN warpdrive base debian  
  
ENV HOME=${WARPDRIVE_APP_ROOT} \  
BASH_ENV=${WARPDRIVE_APP_ROOT}/warpdrive/etc/shell-init \  
ENV=${WARPDRIVE_APP_ROOT}/warpdrive/etc/shell-init \  
PROMPT_COMMAND=". ${WARPDRIVE_APP_ROOT}/warpdrive/etc/shell-init" \  
STI_SCRIPTS_PATH=${WARPDRIVE_S2I_ROOT}/bin \  
PATH=${WARPDRIVE_APP_ROOT}/bin:/usr/local/python/bin:$PATH \  
PYTHONHASHSEED=random  
  
LABEL io.k8s.description="S2I builder for Python web applications." \  
io.k8s.display-name="Python 3.5 (Warp Drive)" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,python,python35,warpdrive,warpdrive-python35" \  
io.openshift.s2i.scripts-url="image://${WARPDRIVE_S2I_ROOT}/bin"  
  
WORKDIR ${WARPDRIVE_SRC_ROOT}  
  
USER 1001  
EXPOSE 8080  
ENTRYPOINT [ "warpdrive", "exec" ]  
CMD [ "warpdrive", "start" ]  

