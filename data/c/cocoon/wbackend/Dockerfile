FROM python:2  
ARG TINI_VERSION="v0.9.0"  
# install tini  
RUN set -x \  
&& export TINI_HOME="/usr/local/sbin" \  
&& curl -fSL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" -o
"${TINI_HOME}/tini" \  
&& curl -fSL
"https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" -o
"${TINI_HOME}/tini.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
&& gpg --batch --verify "${TINI_HOME}/tini.asc" "${TINI_HOME}/tini" \  
&& rm -r "$GNUPGHOME" "${TINI_HOME}/tini.asc" \  
&& chmod +x "${TINI_HOME}/tini" \  
&& "${TINI_HOME}/tini" -h  
  
WORKDIR /usr/local/lib  
  
ADD requirements.txt .  
RUN pip install -r requirements.txt  
  
RUN git clone
https://cocoon_bitbucket@bitbucket.org/cocoon_bitbucket/wbackend.git restop  
RUN mv restop/restop-client/restop_client restop/restop_client  
RUN git clone https://github.com/coleifer/walrus.git walrus  
RUN mv walrus/walrus restop/walrus  
  
ENV PYTHONPATH=/usr/local/lib/restop  
  
EXPOSE 5000  
WORKDIR /usr/local/lib/restop/applications/master  
CMD sleep 5 && python application.py  
  

