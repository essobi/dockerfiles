FROM haskell:7.10  
MAINTAINER Philipp Wagner <mail@philipp-wagner.com>  
  
# Docker does not support mapping the user inside the container to the  
# user running docker when writing to the bind-mounted data volume.  
# This results in all files inside the data volume being owned by root.  
#  
# We work around that by  
# a) passing the UID/GID of the user executing docker as variable  
# b) inside a wrapper script (su_wrapper.sh)  
# - create a new user with this UID/GID  
# - execute the actual ENTRYPOINT script as this user  
#  
# See https://github.com/docker/docker/issues/7198  
ENV HOST_UID 0  
ENV HOST_GID 0  
# Set the env variables to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
# ensure we have a fresh cache to prevent build errors  
RUN apt-get clean  
  
# Configure apt to retry failed downloads  
RUN echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/10retry  
  
# TeXLive  
RUN apt-get update && apt-get install -y \  
texlive-latex-base \  
texlive-fonts-recommended \  
texlive-fonts-extra \  
texlive-latex-extra \  
&& rm -rf /var/lib/apt/lists/*  
  
# package dependencies  
RUN apt-get update && apt-get -y install \  
cabal-install \  
inkscape \  
python3 \  
python-pip \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# pandoc and pandoc-crossref  
# pandoc is automatically installed as dependency of pandoc-crossref  
ENV PANDOC_VERSION "1.17.0.2"  
ENV PANDOC_CROSSREF_VERSION "0.2.1.1"  
RUN cabal update && \  
cabal install --global pandoc-${PANDOC_VERSION} \  
pandoc-crossref-${PANDOC_CROSSREF_VERSION}  
  
# pandocfilters  
RUN pip install pandocfilters  
  
# shared volume: /docs  
WORKDIR /docs  
  
# prepare scripts  
RUN mkdir /opt/osd-doc-converter  
COPY convert.py /opt/osd-doc-converter/convert.py  
RUN chmod +x /opt/osd-doc-converter/convert.py  
COPY pandoc_image_filter.py /opt/osd-doc-converter/pandoc_image_filter.py  
RUN chmod +x /opt/osd-doc-converter/pandoc_image_filter.py  
COPY su_wrapper.sh /opt/osd-doc-converter/su_wrapper.sh  
RUN chmod +x /opt/osd-doc-converter/su_wrapper.sh  
  
# run  
ENTRYPOINT ["/opt/osd-doc-converter/su_wrapper.sh", "/opt/osd-doc-
converter/convert.py"]  
CMD ["--help"]  

