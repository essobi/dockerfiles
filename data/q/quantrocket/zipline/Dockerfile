FROM quantrocket/anaconda3-uwsgi:4.2.0.2  
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
&& curl --insecure -L https://downloads.sourceforge.net/project/ta-lib/ta-
lib/0.4.0/ta-lib-0.4.0-src.tar.gz | tar xvz \  
&& cd ta-lib \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install \  
&& pip install TA-Lib==0.4.14 \  
&& cd /tmp \  
&& rm -r ta-lib  
  
RUN /bin/bash -c "source activate /opt/conda" \  
&& pip install pyfolio==0.8.0 \  
&& pip install theano==0.9.0 \  
&& pip install pymc3==3.1 \  
&& pip install https://codeload.github.com/quantrocket-llc/zipline/zip/master
\  
&& pip install quantrocket-zipline-extensions \  
&& pip install -U quantrocket-client \  
&& /bin/bash -c "source deactivate" \  
&& apt-get update && apt-get install -y g++ # install g++ for theano  
  
ENV UWSGI_WORKERS=1  
COPY qrocket /tmp/uwsgi/qrocket  
COPY uwsgi /etc/uwsgi  
  
RUN mkdir -p /codeload \  
&& mkdir -p /tmp/backtests \  
&& /tmp/build.sh  

