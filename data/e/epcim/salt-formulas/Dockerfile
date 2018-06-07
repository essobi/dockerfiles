#FROM epcim/salty-whales:xenial-2017.7  
#FROM ubuntu:latest  
FROM debian:stretch  
  
MAINTAINER Petr Michalec "<epcim@apealive.net>"  
ARG salt_version="git develop"  
ARG salt_formula_revision="nightly"  
ARG salt_ext_pillar=""  
ENV SALT_BOOTSTRAP_OPTS "-dX ${salt_version}"  
ENV SALT_EXT_PILLAR $salt_ext_pillar  
ENV SALT_FORMULA_REVISION $salt_formula_revision  
ENV LANG C.UTF-8  
ENV LANGUAGE $LANG  
ENV TZ Etc/UTC  
  
#RUN echo "Layer OS upgrade" \  
# && apt-get update -q \  
# && apt-get upgrade -qy \  
# && apt-get clean \  
# && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache /home/*/.cache  
RUN echo "Layer prerequisites and common packages" \  
&& apt-get update -q \  
&& apt-get upgrade -qy \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
gpgv \  
wget \  
curl \  
git \  
sudo \  
python-pip \  
python-wheel \  
python-setuptools \  
python-dev \  
\  
vim-tiny \  
gcc \  
zlib1g-dev \  
apt-transport-https \  
ca-certificates \  
tzdata \  
netcat \  
&& pip install ruamel.yaml \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache /home/*/.cache  
# TODO: once debian update to 0.15.x install python-ruamel.yaml from pkg  
RUN echo "Layer wheelhouse" &&\  
git clone https://github.com/epcim/wheelhouse.git /wh  
  
RUN echo "Layer salt" &&\  
mkdir -p /var/run/salt /var/cache/salt /var/log/salt
/etc/salt/pki/master/minions &&\  
curl -L https://bootstrap.saltstack.com | $SUDO sh -s -- -M
${SALT_BOOTSTRAP_OPTS} &&\  
useradd --system salt &&\  
chown -R salt:salt /etc/salt /var/cache/salt /var/log/salt /var/run/salt &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV APT_REPOSITORY "deb http://apt.mirantis.com/xenial
${salt_formula_revision} salt"  
ENV APT_REPOSITORY_GPG "http://apt.mirantis.com/public.gpg"  
RUN echo "Layer salt-formulas" &&\  
echo "$APT_REPOSITORY" | tee /etc/apt/sources.list.d/salt-formulas.list
>/dev/null &&\  
curl -sL $APT_REPOSITORY_GPG | $SUDO apt-key add - &&\  
apt-get -qq update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -o Dpkg::Options::="--force-
confdef" -o Dpkg::Options::="--force-confold" salt-formula-* -y --fix-missing
;\  
mkdir -p /srv/salt/env/dev ;\  
ln -s /usr/share/salt-formulas/env /srv/salt/env/prd ;\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# alternative:  
#echo "deb http://ppa.launchpad.net/salt-formulas/ppa/ubuntu xenial main"
>/etc/apt/sources.list.d/salt-formulas.list &&\  
#apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
39847281B4B4F5E69A9012612B06BC3AFC7315C0 &&\  
#apt-get update &&\  
#DEBIAN_FRONTEND=noninteractive apt-get install -o Dpkg::Options::="--force-
confdef" -o Dpkg::Options::="--force-confold" salt-formula-* -y &&\  
#apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN echo "Layer reclass" &&\  
mkdir -p /etc/reclass /srv/salt/reclass/classes/system &&\  
git clone https://github.com/Mirantis/reclass-system-salt-model
/srv/salt/reclass/classes/system &&\  
pip install --install-option="--prefix=" \--upgrade --force-reinstall -I \  
git+https://github.com/salt-formulas/reclass.git@develop &&\  
ln -s /usr/share/salt-formulas/reclass/service
/srv/salt/reclass/classes/service  
#apt-get update; DEBIAN_FRONTEND=noninteractive apt-get install -qy reclass &&
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
RUN echo "Layer saltclass" &&\  
mkdir -p mkdir /srv/salt/saltclass/classes/system &&\  
git clone https://github.com/epcim/saltclass-system
/srv/salt/saltclass/classes/system &&\  
cp -a /usr/share/salt-formulas/reclass /usr/share/salt-formulas/saltclass &&\  
for i in $(grep -r -e '^applications:' -e '^parameters:' -l
${SALT_CLASS_SERVICE:-/usr/share/salt-formulas/saltclass/service}); do \  
sed -i 's/applications:/states:/g;s/parameters:/pillars:/g' $i; \  
done &&\  
ln -s /usr/share/salt-formulas/saltclass/service
/srv/salt/saltclass/classes/service  
  
# Use tini as subreaper in Docker container to adopt zombie processes  
ENV TINI_VERSION 0.16.1  
ENV TINI_SHA 5e01734c8b2e6429a1ebcc67e2d86d3bb0c4574dd7819a0aff2dca784580e040  
RUN curl -s -S -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64" -o /bin/tini && chmod +x /bin/tini \  
&& echo "$TINI_SHA /bin/tini" | sha256sum -c -  
  
VOLUME ['/etc/salt/pki' '/srv/salt/env' '/srv/salt/pillar' '/srv/salt/reclass'
'/srv/salt/saltclass']  
  
ADD files/reclass/reclass-config.yml /etc/reclass/  
ADD files/salt/master.conf /etc/salt/master.d/  
# remaining are handled by entrypoint.sh  
ADD files/salt/saltclass.conf /tmp/  
ADD files/salt/reclass.conf /tmp/  
  
EXPOSE 4505 4506  
COPY files/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/bin/tini", "--", "/entrypoint.sh"]  

