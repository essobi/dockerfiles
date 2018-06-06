# Copyright 2016 Kochava  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM alpine:edge  
  
MAINTAINER Kochava  
LABEL Description="Composer Alpine-Linux-based image" Vendor="Kochava"  
  
RUN apk --no-cache upgrade \  
&& apk --no-cache add --upgrade musl openssl git openssh php5-common php5-cli
php5 php5-curl php5-json php5-openssl php5-phar  
  
# Add Composer  
#  
# NB: When updating composer to a new version, ensure that the SHA512SUM  
# variable is updated to match. Otherwise, builds will fail. This should, of  
# course, be updated to a SHA512SUM you trust. If building locally, you can  
# pass the checksum on the CLI.  
ARG COMPOSER_VERSION="1.2.4"  
ARG
COMPOSER_SHA512SUM="781e738eb534fbd4a8dd6c1242c28b617fa9857b3d836c72e0a52db42b48442795a3a5c41ce956988378eee79b0287ff2b3eab30aa4ffcb45b508dad59013bfa"  
ADD https://getcomposer.org/download/$COMPOSER_VERSION/composer.phar
/usr/bin/composer  
RUN ["ash", "-c", "set -e;\necho \"$COMPOSER_SHA512SUM /usr/bin/composer\" |
sha512sum -c || exit 1;\nexec chmod +x /usr/bin/composer", "prepare-composer"]  
  
# Working directory (i.e., place a volume here to install)  
WORKDIR /app  

