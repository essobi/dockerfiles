FROM buildpack-deps:jessie  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
3EC749BE801FDAF13A0C2883426F7E4DB60BBFB8  
  
ENV SSLMATE_VERSION=1.5.1  
ENV SSLMATE_HOST=https://packages.sslmate.com  
  
RUN curl -SLO "${SSLMATE_HOST}/other/sslmate-${SSLMATE_VERSION}.tar.gz" \  
&& curl -SLO "${SSLMATE_HOST}/other/sslmate-${SSLMATE_VERSION}.tar.gz.asc" \  
&& gpg --decrypt sslmate-${SSLMATE_VERSION}.tar.gz.asc \  
&& tar -xvf sslmate-${SSLMATE_VERSION}.tar.gz \  
&& cpan -f -i URI Term::ReadKey JSON::PP \  
&& cd sslmate-${SSLMATE_VERSION}/ \  
&& make install \  
&& rm -vrf /sslmate-${SSLMATE_VERSION}*  

