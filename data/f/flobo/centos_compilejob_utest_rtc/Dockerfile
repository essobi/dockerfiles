FROM flobo/centos_compile_utest:6  
MAINTAINER The U-TEST Team  
  
ENV \  
GITLAB_SSH_PRIVATE_KEY="define" \  
RTC_GIT_PATH=git@gitlab.u-test-factory.org:u-test/rtc_staging.git \  
RTC_GIT_BRANCH_NAME=master \  
\  
RTC_LINUX_TARGET_DIR=linux/rtc/nightbuild-3.0/centos/6/latest \  
RTC_BUILD_DRIVERS=false \  
RTC_REPO=linux/repository/rtc-nightly-latest.repo \  
\  
UTEST_JENKINS_GIT_PATH=git@gitlab.u-test-
factory.org:u-test/jenkins_scripts.git \  
UTEST_JENKINS_GIT_BRANCH_NAME=UTEST_3.0_NG \  
\  
UTEST_EXTERNAL_GIT_PATH=git@gitlab.u-test-
factory.org:u-test/utest_external.git \  
UTEST_EXTERNAL_GIT_BRANCH_NAME=master \  
UTEST_EXTERNAL_LINUX_TARGET_DIR=linux/external/centos/6/ \  
\  
UTEST_DISTRIB_REPO=linux/repository/centos-base.repo \  
UTEST_EXTERNAL_REPO=linux/repository/u-test-external.repo \  
\  
UTEST_VAULT_SERVER_LOGIN="define" \  
UTEST_VAULT_SERVER_PASSWORD="define" \  
UTEST_VAULT_SERVER=https://login:password@vault.u-test-factory.org \  
UTEST_VAULT_SERVER_ROOT_DIR=/ \  
\  
UTEST_NIGHTBUILD_SERVER=u-test-factory.org \  
UTEST_NIGHTBUILD_SERVER_LOGIN="define" \  
UTEST_NIGHTBUILD_SERVER_PORT=22 \  
UTEST_NIGHTBUILD_SERVER_SCP_ROOT_DIR=/var/lib/shasoco/vault.u-test-
factory.org/  
  
COPY build_rtc.sh /build_rtc.sh  
  
ENTRYPOINT ["/build_rtc.sh"]  

