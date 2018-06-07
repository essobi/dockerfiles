FROM groupsky/heimdall  
  
# persistent / runtime deps  
RUN apt-get update && apt-get install -y sudo libqt4-xml libqtcore4 libqtgui4
--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
ENV HEIMDALL_VERSION 1.4.0  
ENV HEIMDALL_FILENAME debian7-heimdall-frontend_1.4.0-0_amd64.deb  
ENV HEIMDALL_SHA256
7752b8f6057fdfb9625ac9ffb940350aa85bc9cfedbe957300a67681497673c1  
  
RUN buildDeps=" \  
curl \  
" \  
&& set -x \  
&& echo "installing prerequisites" \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& echo "downloading heimdall-frontend ${HEIMDALL_VERSION}" \  
&& curl -fSL
"https://bitbucket.org/benjamin_dobell/heimdall/downloads/${HEIMDALL_FILENAME}"
-o "$HEIMDALL_FILENAME" \  
&& echo "$HEIMDALL_SHA256 *$HEIMDALL_FILENAME" | sha256sum -c - \  
&& echo "installing heimdall-frontend $HEIMDALL_VERSION" \  
&& dpkg -i $HEIMDALL_FILENAME \  
&& echo "cleaning up" \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm $HEIMDALL_FILENAME  
  
ENV QT_X11_NO_MITSHM 1  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
ENV HOME /home/developer  
CMD /usr/bin/heimdall-frontend  

