FROM alpine:latest  
RUN BUILD_PKGS="py-pip" \  
&& apk add --no-cache python py-setuptools $BUILD_PKGS \  
&& pip install https://s3.amazonaws.com/cloudformation-examples/aws-cfn-
bootstrap-latest.tar.gz \  
&& apk del --rdepends $BUILD_PKGS  

