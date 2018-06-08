FROM swift:3.0  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
LABEL Description="Swift Perfect Server running on Docker" Vendor="Tommy Lau"
Version="Swift 3.0"  
# Install needed system libraries for MySQL access  
RUN apt-get update \  
&& apt-get install -y libmysqlclient-dev libssl-dev uuid-dev --no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/*  

