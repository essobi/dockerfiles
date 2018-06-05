FROM brightcommerce/ubuntu:14.04.20140911  
MAINTAINER support@brightcommerce.com  
  
# Install curl, git, nodejs and supporting libraries  
RUN apt-get update -q  
RUN apt-get install -qy --force-yes build-essential  
RUN apt-get install -qy --force-yes curl  
RUN apt-get install -qy --force-yes git  
RUN apt-get install -qy --force-yes nodejs  
RUN apt-get install -qy --force-yes zlib1g-dev  
RUN apt-get install -qy --force-yes libssl-dev  
RUN apt-get install -qy --force-yes libreadline-dev  
RUN apt-get install -qy --force-yes libyaml-dev  
RUN apt-get install -qy --force-yes libxml2-dev  
RUN apt-get install -qy --force-yes libxslt-dev  
  
# Install rbenv and ruby-build  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN ./root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
  
# Install multiple versions of ruby  
ENV CONFIGURE_OPTS --disable-install-doc  
ADD ./rubies.txt /root/rubies.txt  
RUN xargs -L 1 rbenv install < /root/rubies.txt  
  
# Install Bundler and rehash for each version of ruby  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
RUN bash -l -c 'for v in $(cat /root/versions.txt); do rbenv global $v; gem
install bundler; rbenv rehash; done'  
  
# Publish port 80  
EXPOSE 80  
# Clean up  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  

