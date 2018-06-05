# Only works with ARM7 devices such as a Raspberry Pi  
FROM multiarch/debian-debootstrap:armhf-jessie  
  
LABEL \  
# org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.name="Google-Assistant" \  
org.label-schema.url="http://www.openhab.com/" \  
# org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/seraphiccorp/docker-google-
assistant.git"  
# Set locales  
ENV \  
LC_ALL=C.UTF-8 \  
LANG=C.UTF-8 \  
LANGUAGE=C.UTF-8  
# Common directory  
VOLUME /google-assistant  
  
# Install packages  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
alsa-utils \  
gcc \  
python3-dev \  
python3-venv \  
portaudio19-dev \  
libffi-dev \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install and set python  
RUN python3 -m venv env \  
&& /env/bin/python -m pip install pip setuptools --upgrade  
  
# Install google-assistant-sdk  
RUN /env/bin/python -m pip install --upgrade
https://github.com/googlesamples/assistant-sdk-
python/releases/download/0.3.0/google_assistant_library-0.0.2-py2.py3-none-
linux_armv7l.whl \  
&& /env/bin/python -m pip install google-assistant-sdk[samples]  
  
# Auhentication (needs user input) and launch google assistant  
CMD cp /google-assistant/asoundrc.config /root/.asoundrc | true \  
&& . /env/bin/activate \  
&& google-oauthlib-tool \  
\--client-secrets /google-assistant/clientid.json \  
\--scope https://www.googleapis.com/auth/assistant-sdk-prototype \  
\--save \  
\--headless \  
&& googlesamples-assistant-hotword

