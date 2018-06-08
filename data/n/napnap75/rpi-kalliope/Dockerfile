FROM resin/armv7hf-debian:stretch  
  
RUN [ "cross-build-start" ]  
  
RUN sed -i 's/stretch main/stretch main contrib non-free/'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends git python-dev libsmpeg0
libttspico-utils libsmpeg0 flac dialog libffi-dev libffi-dev libssl-dev
portaudio19-dev build-essential libssl-dev libffi-dev sox libatlas3-base
mplayer libav-tools python-pip python-yaml python-pyaudio python-cffi python-
crypto python-pycparser python-itsdangerous python-nacl python-aniso8601
python-setuptools python-wheel python-markupsafe python-dialog && \  
rm -rf /var/lib/apt/lists/* && \  
sudo pip install kalliope && \  
useradd kalliope --home /kalliope  
  
RUN [ "cross-build-end" ]  
  
USER kalliope  
VOLUME /kalliope  
WORKDIR /kalliope  
CMD [ "kalliope start" ]  

