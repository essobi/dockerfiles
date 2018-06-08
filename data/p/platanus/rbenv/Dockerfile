FROM platanus/apt  
  
MAINTAINER Juan Ignacio Donoso "juan.ignacio@platan.us"  
  
# Env variable to make rbenv work  
ENV HOME /root  
ENV RBENV_ROOT /usr/local/rbenv  
ENV PATH ${RBENV_ROOT}/bin:${RBENV_ROOT}/shims:${PATH}  
  
# Install rbenv  
RUN cd /usr/local && \  
curl -L https://github.com/sstephenson/rbenv/archive/v0.4.0.tar.gz | tar xz &&
\  
mv rbenv-0.4.0 rbenv  
  
# Install rbenv vars plugin  
RUN mkdir -p /usr/local/rbenv/plugins && \  
cd /usr/local/rbenv/plugins && \  
curl -L https://github.com/sstephenson/rbenv-vars/archive/v1.2.0.tar.gz | tar
xz && \  
mv rbenv-vars-1.2.0 rbenv-vars  
  
# Install ruby build rbenv gem-rehash plugin  
RUN mkdir -p /usr/local/rbenv/plugins && \  
cd /usr/local/rbenv/plugins && \  
curl -L https://github.com/sstephenson/rbenv-gem-rehash/archive/v1.0.0.tar.gz
| tar xz && \  
mv rbenv-gem-rehash-1.0.0 rbenv-gem-rehash  
  
# Install ruby build rbenv plugin  
RUN mkdir -p /usr/local/rbenv/plugins && \  
cd /usr/local/rbenv/plugins && \  
curl -L https://github.com/sstephenson/ruby-build/archive/v20150303.tar.gz |
tar xz && \  
mv ruby-build-20150303 ruby-build  

