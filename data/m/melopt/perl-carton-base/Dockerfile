FROM perl  
MAINTAINER Pedro Melo <melo@simplicidade.org>  
  
## Bootstrap what we need  
RUN apt-get update -y \  
&& cpanm -q -n Carton \  
&& rm -rf "$HOME/.cpanm" \  
&& /usr/sbin/useradd -m -d /app -s /bin/nologin -U app \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y  
  
## Copy our magic scripts  
COPY base-entrypoint run-docker-build-hook install-deps /usr/sbin/  
RUN chmod 555 \  
/usr/sbin/base-entrypoint \  
/usr/sbin/run-docker-build-hook \  
/usr/sbin/install-deps  
  
## Saner/safer defaults  
WORKDIR /app  
ENV APP_HOMEDIR /app  
  
## Make application lib's available out-of-the-box  
## This requires the entrypoint script below  
ENV APP_PERL5LIB /app/lib  
  
## Define entrypoint  
ENTRYPOINT ["/usr/sbin/base-entrypoint"]  
ENV BASE_ENTRYPOINT "/usr/sbin/base-entrypoint"  
ENV BASE_DEPS "/deps/local"  
ENV BASE_PERL5LIB "$BASE_DEPS/lib/perl5"  
## Set a decent default CMD... Each person will override it to taste, I'm
sure.  
CMD ["/bin/bash"]  
  
### Our build process  
## Init the hook system  
ONBUILD COPY .docker-build-hooks/ /build/.docker-build-hooks/  
ONBUILD RUN /usr/sbin/run-docker-build-hook after-init-hooks  
  
## Install you app dependencies  
ONBUILD RUN /usr/sbin/run-docker-build-hook before-dependencies-install  
ONBUILD COPY cpanfile cpanfile.snapshot /deps/  
ONBUILD RUN /usr/sbin/install-deps \  
&& /usr/sbin/run-docker-build-hook after-dependencies-install  
  
## Copy your app files  
ONBUILD RUN /usr/sbin/run-docker-build-hook before-app-copy  
ONBUILD COPY . /app  
ONBUILD RUN /usr/sbin/run-docker-build-hook after-app-copy \  
&& chown app:app .  
  
## From this point on, we run as 'app'  
ONBUILD USER app  

