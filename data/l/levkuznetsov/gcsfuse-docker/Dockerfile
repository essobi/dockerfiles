# The MIT License (MIT)  
# Copyright (c) 2017 lev.v.kuznetsov@gmail.com  
#  
# Permission is hereby granted, free of charge, to any person  
# obtaining a copy of this software and associated documentation  
# files (the "Software"), to deal in the Software without  
# restriction, including without limitation the rights to use,  
# copy, modify, merge, publish, distribute, sublicense, and/or  
# sell copies of the Software, and to permit persons to whom the  
# Software is furnished to do so, subject to the following  
# conditions:  
#  
# The above copyright notice and this permission notice shall be  
# included in all copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES  
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND  
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT  
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,  
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR  
# OTHER DEALINGS IN THE SOFTWARE.  
FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget autofs \  
&& echo "deb http://packages.cloud.google.com/apt cloud-sdk-xenial main" | tee
/etc/apt/sources.list.d/google-cloud.sdk.list \  
&& echo "deb http://packages.cloud.google.com/apt gcsfuse-xenial main" | tee
/etc/apt/sources.list.d/gcsfuse.list \  
&& wget -qO- https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key
add - \  
&& apt-get update && apt-get install -y --no-install-recommends google-cloud-
sdk gcsfuse \  
&& mkdir -p /etc/autofs && touch /etc/autofs/auto.gcsfuse && rm -rf
/var/lib/apt/lists  
  
ADD auto.master /etc/auto.master  
  
WORKDIR /mnt  
  
VOLUME /mnt  
VOLUME /etc/gcloud  
VOLUME /etc/autofs  
  
ENV GOOGLE_APPLICATION_CREDENTIALS /etc/gcloud/service-account.json  
  
CMD ["/usr/sbin/automount", "-t", "0", "-f", "/etc/auto.master"]  

