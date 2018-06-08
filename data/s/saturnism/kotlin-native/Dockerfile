# Copyright 2018 Google Inc.  
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
FROM openjdk:8u171  
  
ENV KOTLIN_NATIVE_VERSION 0.7  
RUN cd /opt && curl -L https://github.com/JetBrains/kotlin-
native/releases/download/v${KOTLIN_NATIVE_VERSION}/kotlin-native-
linux-${KOTLIN_NATIVE_VERSION}.tar.gz | tar -xz  
RUN ln -sf /opt/kotlin-native-linux-${KOTLIN_NATIVE_VERSION} /opt/kotlin-
native  
RUN /opt/kotlin-native/bin/kotlinc-native --check_dependencies && rm -rf
/root/.konan/cache  
  
ENV PATH $PATH:/opt/kotlin-native/bin  
  
ENTRYPOINT ["kotlinc"]  

