FROM felix11h/neuroenv_smt
MAINTAINER Felix Z. Hoffmann <felix11h.dev@gmail.com>

# Adapted from Ivo Jimenez
RUN apt-get -yq update && \
    apt-get install -qy --fix-missing \
        texlive \
        texlive-latex-extra \
	texlive-science \
        texlive-math-extra \
	dvipng && \
    apt-get -yq autoremove && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

