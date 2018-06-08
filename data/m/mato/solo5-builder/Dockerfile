#  
# Architecture-independent Docker image for container-based Solo5 CI nodes.  
#  
# "builder" stage  
#  
FROM debian:stretch AS builder  
#  
# Installs surf-build from Git, version is set here:  
ARG SURF_VERSION=2.0.0-beta.4  
#  
# Install dependencies.  
# "file" is required(?) by various npm scripts.  
#  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq -y \  
\--no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
file \  
git \  
gnupg \  
&& apt-get clean  
#  
# Add NodeSource repository key and install Node.js.  
#  
RUN curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key \  
| apt-key add - && \  
echo "deb https://deb.nodesource.com/node_8.x stretch main" \  
| tee /etc/apt/sources.list.d/nodesource.list  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq -y \  
\--no-install-recommends \  
nodejs \  
&& apt-get clean  
#  
# Create a non-root user, otherwise npm somehow manages to succeed in building  
# a package but does not actually compile the .ts files into it. What is this
I  
# don't even ...  
#  
RUN useradd -u 1000 -g users -d /home/build -m -s /bin/bash build  
USER build  
WORKDIR /home/build  
#  
# Clone surf-build, compile and pack into tarball.  
# This particular part of the build must not run as root (see above) or be run  
# with "-g" since both cases WILL cause failures with unhelpful error messages  
# or none at all!  
#  
# Use --no-optional to prevent npm trying to install yet more useless  
# dependencies and verbosely spewing pages of errors when it fails.  
#  
RUN git clone \--depth=1 https://github.com/surf-build/surf  
RUN cd surf && git checkout v${SURF_VERSION} && \  
npm install --no-optional && npm pack && \  
cp surf-build-${SURF_VERSION}.tgz /tmp/surf-build.tar.gz  
  
#  
# "ci" stage  
#  
FROM debian:stretch AS ci  
#  
# Install dependencies.  
#  
# "iputils-ping" is needed to replace "inetutils-ping" due to  
# https://github.com/debuerreotype/docker-debian-artifacts/issues/36  
#  
# "qemu-system-x86" is only used on x86_64 for the virtio tests.  
#  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq -y \  
\--no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
file \  
git \  
gnupg \  
linux-libc-dev \  
iputils-ping \  
$([ `uname -m` = x86_64 ] && echo qemu-system-x86) \  
&& apt-get clean  
#  
# Install dumb-init for correct operation as container PID 1  
#  
# Build from source so that we don't have to care which architecture we're on.  
#  
RUN curl -L --silent https://github.com/Yelp/dumb-init/archive/v1.2.0.tar.gz
-o /tmp/dumb-init.tar.gz \  
&& tar -C /tmp -xzf /tmp/dumb-init.tar.gz \  
&& make -C /tmp/dumb-init-1.2.0 \  
&& cp /tmp/dumb-init-1.2.0/dumb-init /usr/bin \  
&& rm -r /tmp/dumb-init-1.2.0 /tmp/dumb-init.tar.gz  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
#  
# Add NodeSource repository key and install Node.js.  
#  
RUN curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key \  
| apt-key add - && \  
echo "deb https://deb.nodesource.com/node_8.x stretch main" \  
| tee /etc/apt/sources.list.d/nodesource.list  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qq -y \  
\--no-install-recommends \  
nodejs \  
&& apt-get clean  
#  
# Install surf-build using the packaged tarball we built earlier.  
#  
# Use --no-optional to prevent npm trying to install yet more useless  
# dependencies and verbosely spewing pages of errors when it fails.  
# --unsafe-perm is needed to work around meaningless npm failure with "EACCES"  
# when installing dugite.  
#  
COPY \--from=builder /tmp/surf-build.tar.gz /tmp/surf-build.tar.gz  
RUN npm install -g --unsafe-perm --no-optional /tmp/surf-build.tar.gz && rm -f
/tmp/surf-build.tar.gz  
  
# XXX Add LOCAL_GIT_DIRECTORY=/usr GIT_EXEC_PATH=/usr/lib/git-core to  
# environment to force dugite to use system Git instead of a random binary
from  
# the Internet?  
# Needed to get Git credentials passed through correctly when uploading the
build log as a gist.  
RUN ln -s /usr/lib/node_modules/surf-build/node_modules/.bin/git-askpass-env \  
/usr/local/bin/git-askpass-env  
  
#  
# Run the builder.  
#  
# We don't set a specific CMD here; the driver script will run the appropriate  
# surf-build command.  
CMD ["/bin/bash"]  

