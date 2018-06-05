FROM ruby:2.3.5  
MAINTAINER Jason Cox <jason.cox@panoply.fm>  
  
# Install dependencies.  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
pigz python-pip unzip  
RUN pip install -U crcmod  
  
RUN \  
wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip -qO
/tmp/google-cloud-sdk.zip && \  
unzip -qd /usr/local /tmp/google-cloud-sdk.zip && \  
/usr/local/google-cloud-sdk/install.sh --usage-reporting=false \--path-
update=false \--bash-completion=false && \  
rm -rf /tmp/google-cloud-sdk.zip  
ENV PATH /usr/local/google-cloud-sdk/bin:$PATH  
RUN touch /etc/boto.cfg  
RUN gcloud components install kubectl  
  
# Setup app directory.  
RUN mkdir /builder  
WORKDIR /builder  
  
# Copy the Gemfile & Gemfile.lock and install gems before the project is
copied - avoids unnecessary bundle installs.  
COPY Gemfile /builder/Gemfile  
COPY Gemfile.lock /builder/Gemfile.lock  
RUN bundle install --without development test doc --jobs=4  
  
ADD . /builder  
ADD docker-init.sh /usr/local/bin/docker-init.sh  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# allow ssh config  
RUN curl -fL "https://raw.githubusercontent.com/buildkite/docker-ssh-env-
config/d06f20bdc7457a647bfe3724d94525f83c863091/ssh-env-config.sh" -o
/usr/local/bin/ssh-env-config.sh \  
&& chmod +x /usr/local/bin/ssh-env-config.sh  
  
RUN chmod +x /usr/local/bin/docker-init.sh  
ENTRYPOINT ["docker-init.sh"]  

