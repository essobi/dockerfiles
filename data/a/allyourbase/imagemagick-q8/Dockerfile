# Start with public magickdeps image  
FROM allyourbase/magickdeps  
  
# Install ImageMagick with PerlMagick module  
ENV MAGICK_VER 6.8.9-10  
RUN apt-get -y update && apt-get install -y --no-install-recommends \  
libperl-dev \  
&& cd /tmp \  
&& curl -L -O
http://www.imagemagick.org/download/releases/ImageMagick-${MAGICK_VER}.tar.xz
\  
&& tar -xf ImageMagick-${MAGICK_VER}.tar.xz \  
&& cd ImageMagick-${MAGICK_VER} \  
&& ./configure --enable-shared --with-gslib --with-wmf --without-x --with-xml
\  
\--with-freetype --with-fontconfig --with-quantum-depth=8 --with-
perl=/usr/bin/perl \  
&& make && make install && make clean \  
&& ldconfig \  
&& cd /tmp \  
&& rm -rf ImageMagick-${MAGICK_VER}* \  
&& apt-get -y purge libperl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY policy.xml /usr/local/etc/ImageMagick-6/policy.xml  
  
# add Git SHA label to image build  
ARG GIT_COMMIT=unknown  
LABEL org.label-schema.vcs-ref=$GIT_COMMIT  
  
WORKDIR /  
  
CMD ["convert", "--version"]  

