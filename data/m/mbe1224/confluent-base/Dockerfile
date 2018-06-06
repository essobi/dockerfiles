FROM mbe1224/debian-oracle-java:jessie-slim-jdk8  
  
ARG CONFLUENT_DEB_REPO="http://packages.confluent.io"  
ARG APT_ALLOW_UNAUTHENTICATED=false  
ENV APT_ALLOW_UNAUTHENTICATED=${APT_ALLOW_UNAUTHENTICATED}  
  
ENV PYTHON_VERSION="2.7.9-1"  
ENV PYTHON_PIP_VERSION="9.0.1"  
ENV SCALA_VERSION="2.11"  
ENV CONFLUENT_MAJOR_VERSION="3"  
ENV CONFLUENT_MINOR_VERSION="3"  
ENV CONFLUENT_PATCH_VERSION="0"  
ENV
CONFLUENT_VERSION="$CONFLUENT_MAJOR_VERSION.$CONFLUENT_MINOR_VERSION.$CONFLUENT_PATCH_VERSION"  
ENV CONFLUENT_DEB_VERSION="1"  
ENV KAFKA_VERSION="0.11.0.0"  
ENV COMMIT_SHA="d779b0c5c17bb75a8cbd5b61e11c7e954ef2211d"  
ENV LANG="C.UTF-8"  
RUN echo "===> Updating debian ....." \  
&& apt-get -qq update \  
&& echo "===> Installing curl wget netcat python...." \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https curl
wget netcat python=${PYTHON_VERSION} \  
&& echo "===> Installing python packages ..." \  
&& curl -fSL "https://bootstrap.pypa.io/get-pip.py" | python \  
&& pip install --no-cache-dir --upgrade pip==${PYTHON_PIP_VERSION} \  
&& pip install --no-cache-dir jinja2 requests \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "===> Adding confluent
repository...${CONFLUENT_DEB_REPO}/deb/${CONFLUENT_MAJOR_VERSION}.${CONFLUENT_MINOR_VERSION}"
\  
&& if [ "x$APT_ALLOW_UNAUTHENTICATED" = "xtrue" ]; then echo
"APT::Get::AllowUnauthenticated \"true\";" >
/etc/apt/apt.conf.d/allow_unauthenticated; else curl -L
${CONFLUENT_DEB_REPO}/deb/${CONFLUENT_MAJOR_VERSION}.${CONFLUENT_MINOR_VERSION}/archive.key
| apt-key add - ; fi \  
&& echo "deb [arch=amd64]
${CONFLUENT_DEB_REPO}/deb/${CONFLUENT_MAJOR_VERSION}.${CONFLUENT_MINOR_VERSION}
stable main" >> /etc/apt/sources.list \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/base/include/cub" -O "/usr/local/bin/cub" \  
&& wget "https://raw.githubusercontent.com/confluentinc/cp-docker-
images/${COMMIT_SHA}/debian/base/include/dub" -O "/usr/local/bin/dub" \  
&& chmod a+x "/usr/local/bin/cub" \  
&& chmod a+x "/usr/local/bin/dub"  
COPY include/etc/confluent/docker/docker-utils.jar
/etc/confluent/docker/docker-utils.jar

