FROM debian:sid-slim  
MAINTAINER David Sferruzza <david.sferruzza@gmail.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install LaTeX tools  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
texlive-full \  
biber \  
curl \  
python-pygments \  
# Remove documentation packages  
&& apt-get --purge -y remove \  
texlive-fonts-extra-doc \  
texlive-fonts-recommended-doc \  
texlive-humanities-doc \  
texlive-latex-base-doc \  
texlive-latex-extra-doc \  
texlive-latex-recommended-doc \  
texlive-metapost-doc \  
texlive-pictures-doc \  
texlive-pstricks-doc \  
texlive-publishers-doc \  
texlive-science-doc \  
# Slim down image  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/??
/usr/share/man/??_*  
  
# Add the latest latexmk  
COPY latexmk /usr/local/bin/  

