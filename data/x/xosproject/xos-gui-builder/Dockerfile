  
# Copyright 2017-present Open Networking Foundation  
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
# To build use: docker build -t xosproject/xos-gui-builder:candidate .  
FROM node:7.9.0  
  
# Set environment vars  
ENV CODE_SOURCE .  
ENV CODE_DEST /var/www  
  
RUN mkdir -p ${CODE_DEST}  
  
COPY ${CODE_SOURCE}/package.json ${CODE_SOURCE}/typings.json ${CODE_DEST}/  
  
WORKDIR ${CODE_DEST}  
RUN npm install \  
&& npm run typings  
  
ARG org_label_schema_schema_version=1.0  
ARG org_label_schema_name=xos-gui-builder  
ARG org_label_schema_version=unknown  
ARG org_label_schema_vcs_url=unknown  
ARG org_label_schema_vcs_ref=unknown  
ARG org_label_schema_build_date=unknown  
ARG org_opencord_vcs_commit_date=unknown  
  
LABEL org.label-schema.schema-version=$org_label_schema_schema_version \  
org.label-schema.name=$org_label_schema_name \  
org.label-schema.version=$org_label_schema_version \  
org.label-schema.vcs-url=$org_label_schema_vcs_url \  
org.label-schema.vcs-ref=$org_label_schema_vcs_ref \  
org.label-schema.build-date=$org_label_schema_build_date \  
org.opencord.vcs-commit-date=$org_opencord_vcs_commit_date  

