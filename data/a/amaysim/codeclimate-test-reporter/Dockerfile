FROM alpine:3.7  
LABEL maintainer "@flemay"  
RUN apk --update --no-cache add git make  
ENV CC_TEST_REPORTER_VERSION=0.5.0  
ENV CC_TEST_REPORTER_URL https://codeclimate.com/downloads/test-reporter/test-
reporter-${CC_TEST_REPORTER_VERSION}-linux-amd64  
ENV CC_TEST_REPORTER_NAME cc-test-reporter  
RUN wget -O ${CC_TEST_REPORTER_NAME} ${CC_TEST_REPORTER_URL} && chmod +x
${CC_TEST_REPORTER_NAME}  
ENTRYPOINT [ "/cc-test-reporter" ]

