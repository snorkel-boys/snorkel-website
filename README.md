스노클 웹사이트 프로젝트

0. 룰
- 누구나 다 수정할 수 있으니 맘에 안드는 내용들 수정할 것
- 기획안과 다른 내용 수정시 멤버들 동의를 구할 것

1. 기획안
- 구상

2. 진행상황 공유
-  18.3.23 : 헤로쿠 세팅 완료, 기본적인 레이아웃 구축 중 / 선진
-

3. 건의사항 or 아이디어

4. 헤로쿠(Heroku) 주소
- https://snorkel-boys.herokuapp.com
- 30분간 트래픽이 없으면 서버를 종료하는 형식이니 처음에 접속하면 느릴 수도 있음

5. 간단한 깃 사용법
- 기본적인 구조
  - git add .로 stage에 올리고 git commit -m "수정사항"으로 커밋을 한 다음에
  - git push origin master하면 각자의 컴퓨터 수정파일이 멤버들 개인 repository로 업로드 됨
  - https://github.com/snorkel-boys/snorkel-website 로 가서 Pull Request 클릭
  - Create Pull Request하면 공동 repository에 커밋한 사항이 저장이 됨!
- 내 컴퓨터로 다운받기
  - https://github.com/snorkel-boys/snorkel-website 에서 내 repository(저장소)로 Fork(복사)을 한다
  - https://github.com/내아이디/snorkel-website로 가서 복사된 프로젝트를 내 컴퓨터로 다운 : git clone https://github.com/내아이디/snorkel-website
- Branch 파기
  - 각자 수정할때 Master Branch에 푸쉬하지 말고 따로 수정하는 기능의 브랜치를 만들어서 나중에 Master에 merge할 것.(오류 방지)
  - git branch(브랜치 보기)
  - git branch something(something 이라는 브랜치 생성)
  - git checkout something(something 이라는 브랜치로 이동)
  - 커밋(세부과정 생략)
  - https://github.com/snorkel-boys/snorkel-website 로 가서 Pull Request 클릭
  - Create Pull Request하면 공동 repository에 커밋한 사항이 저장이 됨!
- 수정된 버전 다시 받기
  - 다른 사람이 커밋해서 풀리퀘스트까지 받아들여져 프로젝트 반영이 되면 내 로컬컴퓨터에 있는 파일과 내용이 달라지기때문에 수시로 업데이트된 내용 받아올 것
  - git pull origin master
