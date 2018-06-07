FROM ubuntu:14.04  
  
RUN \  
apt-get update -q && \  
env DEBIAN_FRONTEND=noninteractive apt-get install -qy \--no-install-
recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
iptables \  
openssh-client \  
xz-utils && \  
apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
echo 'deb https://get.docker.com/ubuntu docker main' >
/etc/apt/sources.list.d/docker.list && \  
apt-get update -q && \  
env DEBIAN_FRONTEND=noninteractive apt-get install -qy \--no-install-
recommends lxc-docker-1.7.1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
mkdir -p /tmp/src && \  
cd /tmp/src && \  
curl -fsSL -O
https://raw.githubusercontent.com/jpetazzo/dind/e253b43366abf618475237e15633c43dc2ad40e6/wrapdocker
&& \  
curl -fsSL -o docker-compose
https://github.com/docker/compose/releases/download/1.3.3/docker-compose-
Linux-x86_64 && \  
curl -fsSL -o buildkite-agent.tar.gz
https://github.com/buildkite/agent/releases/download/v2.1-beta.2/buildkite-
agent-linux-amd64-2.1-beta.2.tar.gz && \  
echo '09db4aec4be5e213c058d8585ff41f1d765f7fbaf42c18e80d91a1126f9a4f60
wrapdocker' | sha256sum -c && \  
echo '97ce4770d4857731d952af492800f2fcc3199e8c40b146b994ca48a912e0450c docker-
compose' | sha256sum -c && \  
echo '8426f8c71f55e3467b6f654e1b8fe527bd8ea135e12dbbafce0a66937d5c36e7
buildkite-agent.tar.gz' | sha256sum -c && \  
mv wrapdocker docker-compose /usr/local/bin && \  
chmod 0755 /usr/local/bin/wrapdocker /usr/local/bin/docker-compose && \  
mkdir -p /buildkite/bin /buildkite/hooks && \  
tar -C /buildkite -xzf buildkite-agent.tar.gz ./bootstrap.sh ./buildkite-
agent.cfg && \  
tar -C /buildkite/bin -xzf buildkite-agent.tar.gz ./buildkite-agent && \  
chmod 0755 /buildkite/bootstrap.sh /buildkite/bin/buildkite-agent && \  
cd /tmp && \  
rm -rf /tmp/src  
  
ENV \  
PATH=/buildkite/bin:"$PATH" \  
BUILDKITE_BOOTSTRAP_SCRIPT_PATH=/buildkite/bootstrap.sh \  
BUILDKITE_BUILD_PATH=/buildkite/builds \  
BUILDKITE_HOOKS_PATH=/buildkite/hooks  
# Internal docker runs out of a volume  
VOLUME /var/lib/docker  
  
ENTRYPOINT ["wrapdocker", "buildkite-agent"]  
CMD ["start"]  

