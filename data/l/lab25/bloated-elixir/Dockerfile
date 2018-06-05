FROM elixir:1.6-slim  
  
ARG WKHTMLTOPDF_VERSION=0.12.4  
ARG
WKHTMLTOPDF_CHECKSUM=049b2cdec9a8254f0ef8ac273afaf54f7e25459a273e27189591edc7d7cf29db  
  
# Install Rebar and Hex  
RUN set -xe; \  
mix local.rebar --force;\  
mix local.hex --force;  
  
# Some mix tasks require git for dependency checks  
RUN set -xe; \  
apt-get update; \  
apt-get install -y --no-install-recommends git; \  
rm -rf /var/lib/apt/lists/*  
# Install wkhtmltopdf  
RUN set -xe; \  
apt-get update; \  
apt-get install -y --no-install-recommends libxrender1 libfontconfig1 libXext6
ca-certificates curl xz-utils; \  
mkdir -p /tmp/wkhtmltopdf; \  
cd /tmp/wkhtmltopdf; \  
echo "$WKHTMLTOPDF_CHECKSUM wkhtmltopdf.tar.xz" > checksum.txt; \  
curl -L -o wkhtmltopdf.tar.xz
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/${WKHTMLTOPDF_VERSION}/wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-
generic-amd64.tar.xz; \  
sha256sum --check checksum.txt; \  
tar xf wkhtmltopdf.tar.xz; \  
cp wk*/bin/wkhtmltopdf /usr/bin; \  
cd /; \  
rm -rf /tmp/wkhtmltopdf; \  
apt-get purge --auto-remove -y ca-certificates curl xz-utils; \  
rm -rf /var/lib/apt/lists/*  

