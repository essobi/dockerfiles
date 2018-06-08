FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
# Install ta-lib  
RUN apt-get -y update && apt-get -y install \  
build-essential \  
libfreetype6-dev \  
libpng-dev \  
libopenblas-dev \  
liblapack-dev \  
gfortran \  
&& cd /tmp \  
&& curl -L https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-
lib-0.4.0-src.tar.gz | tar xvz \  
&& cd ta-lib \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& pip install TA-Lib==0.4.14 \  
&& cd /tmp \  
&& rm -r ta-lib  
  
RUN /bin/bash -c "source activate /opt/conda" \  
&& pip install quantrocket-moonshot \  
&& pip install quantrocket-moonchart \  
&& pip install -U quantrocket-client \  
&& /bin/bash -c "source deactivate"  
  
ENV UWSGI_WORKERS=3 MOONSHOT_DIR=/codeload/moonshot
MOONSHOT_CACHE_DIR=/tmp/cache  
COPY qrocket /tmp/uwsgi/qrocket  
COPY uwsgi /etc/uwsgi  
  
RUN mkdir -p /codeload \  
&& mkdir -p /tmp/backtests \  
&& mkdir -p /tmp/cache \  
&& mkdir -p /tmp/orders \  
&& /tmp/build.sh  

