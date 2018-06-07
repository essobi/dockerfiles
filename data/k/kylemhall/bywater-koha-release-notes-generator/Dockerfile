FROM perl:5.26  
LABEL maintainer="kyle@bywatersolutions.com"  
  
ENV DEBUG 0  
ENV KOHACLONE /kohaclone  
ENV UPLOAD 1  
#ENV GITHUB_TOKEN  
#ENV KOHA_BRANCH  
WORKDIR /app  
ADD . /app  
  
RUN apt-get -y update \  
&& apt-get -y install \  
vim \  
git-core \  
libssl-dev \  
libmodern-perl-perl \  
librest-client-perl \  
libjson-perl \  
libtemplate-perl \  
libcrypt-ssleay-perl \  
liblwp-protocol-https-perl  
  
RUN git clone \--origin bws-production
https://github.com/bywatersolutions/bywater-koha.git $KOHACLONE  
  
CMD ./generate_release_notes.pl  

