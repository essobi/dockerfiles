FROM ruby:2.4-jessie  
  
ENV SERVICE_ROOT /service  
ENV SERVICE_USER service  
ENV YARN_VERSION 0.22.0  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
  
RUN apt-get update -qq \  
&& apt-get -y install build-essential libpq-dev libqt4-dev git wget \  
libyaml-dev postgresql-client-9.4 xvfb nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \  
done \  
&& curl -fSL -o yarn.js "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js" \  
&& curl -fSL -o yarn.js.asc "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-
legacy-$YARN_VERSION.js.asc" \  
&& gpg --batch --verify yarn.js.asc yarn.js \  
&& rm yarn.js.asc \  
&& mv yarn.js /usr/local/bin/yarn \  
&& chmod +x /usr/local/bin/yarn  
  
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-
bootstrap/master/install.sh /tmp/consul_template_install.sh  
RUN bash /tmp/consul_template_install.sh && rm /tmp/consul_template_install.sh  
  
RUN groupadd $SERVICE_USER && useradd --create-home --home $SERVICE_ROOT
\--gid $SERVICE_USER \--shell /bin/bash $SERVICE_USER  
WORKDIR $SERVICE_ROOT  
  
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-
bootstrap/master/wait-for-it.sh /wait-for-it.sh  
RUN chmod a+rx /wait-for-it.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

