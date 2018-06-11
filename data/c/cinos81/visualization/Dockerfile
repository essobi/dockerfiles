# 우분투 이미지 시작  
FROM ubuntu  
  
ENV version=1.0  
# 라이브러리 업데이트 & 설치  
RUN apt-get update -yqq && apt-get install build-essential libssl-dev git curl
sudo libpng-dev -yqq  
  
# node.js 최신버전 설치  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && apt-get
update -yqq && apt-mark unhold npm && apt-get install nodejs -yqq  
  
# git 디렉토리 생성  
RUN mkdir -p git  
  
# git 디렉토리로 이동  
WORKDIR git  
  
# 리소스 크리에이터 내려받기  
RUN git clone https://bitbucket.org/lucisfrontendteam/resourcecreator  
  
# api 테스터 내려받기  
RUN git clone https://bitbucket.org/lucisfrontendteam/apiverifier  
  
# 프로젝트 플레이어 내려받기  
RUN git clone https://bitbucket.org/lucisfrontendteam/userdashboard  
  
# 관리자 프로젝트 내려받기  
RUN git clone https://bitbucket.org/lucisfrontendteam/uicontentsmanager  
  
# 문서 프로젝트 내려받기  
RUN git clone https://bitbucket.org/lucisfrontendteam/documents  
  
# 마크업 프로젝트 내려받기  
RUN git clone https://bitbucket.org/lucisfrontendteam/dashboard
/git/documents/Markup  
  
# resourcecreator 디렉토리로 이동  
WORKDIR /git/resourcecreator  
  
# 리소스 크리에이터의 라이브러리 인스톨  
RUN npm install  
  
# apiverifier 디렉토리로 이동  
WORKDIR /git/apiverifier  
  
# api 테스터의 라이브러리 인스톨  
RUN npm install  
  
# uicontentsmanager 디렉토리로 이동  
WORKDIR /git/uicontentsmanager  
  
# uicontentsmanager의 라이브러리 인스톨  
RUN npm install  
  
# userdashboard 디렉토리로 이동  
WORKDIR /git/userdashboard  
  
# 프로젝트 플레이어의 라이브러리 인스톨  
RUN npm install  
  
# documents 디렉토리로 이동  
WORKDIR /git/documents  
  
# 문서프로젝트의 라이브러리 인스톨  
RUN npm install  
  
# resourcecreator 디렉토리로 이동  
WORKDIR /git/resourcecreator  
  
# 리소스 크리에이터를 오프라인 모드로 빌드  
RUN npm run pub  
  
# 리소스 크리에이터를 리소스 모드로 빌드  
RUN npm run build  
  
# userdashboard 디렉토리로 이동  
WORKDIR /git/userdashboard  
  
# 프로젝트 플레이어를 오프라인 모드로 빌드  
RUN npm run pub  
  
# apiverifier 디렉토리로 이동  
WORKDIR /git/apiverifier  
  
# api 테스터를 오프라인 모드로 빌드  
RUN npm run pub  
  
# uicontentsmanager 디렉토리로 이동  
WORKDIR /git/uicontentsmanager  
  
# uicontentsmanager를 오프라인 모드로 빌드  
RUN npm run pub  
  
# resourcecreator 디렉토리로 이동  
WORKDIR /git/resourcecreator  
  
# api 문서 빌드  
RUN npm run doc  
  
# documents 디렉토리로 이동  
WORKDIR /git/documents  
  
# 포트 개방  
EXPOSE 8080  
# 오프라인 모드 인스턴스 실행  
CMD npm start  
  

