# 환경설정
```bash
$ pip install -r requirements.txt
```
Django와 black을 설치합니다.

# 가상환경 설정
가상환경 이름을 'penny-venv'로 설정해주세요. 

# base.html
일단 네브바 색깔때문에 설정 안했습니다. 

# models.py
어떤 데이터가 들어갈지 모르겠어서 일단 title, content만 넣었어요.

# Clone
포크뜨지 않고 클론만 해주세여! 

# 작업 시 주의사항
3명이 동시에 작업할 수는 없는 것 같아요 (방법 알아봅시당)
만약 작업을 시작한다면 '시작할게요!' 라고 말해주세요.
나머지 2명은 작업자가 작업을 끝내고 push할 때 까지 클론한 파일을 건들면 안돼요!

% 꼭 작업 시작과 끝냄을 공지해주셔야 합니다! %
마무리할 시 꼭 push로 작업을 마무리해주세요!

(나의 컴퓨터에 저장되어있는 코드들과 pull 당겨올 시 전 작업과 동일하지 않으면 충돌이 나서 pull할 수 없어요!
만약 충돌이 났다면 본인의 폴더를 모두 지우고 다시 클론받아주세요.
이 경우 본인이 작업한 코드들을 다시 작성해주셔야 합니다.
꼭 조심해주세욤~!)

# Github 저장소 Mirror하는 법

### 1. 깃허브 새로운 저장소 생성

2번 개발자는 새로운 저장소를 생성합니다.

### 2. 1번 개발자 저장소 clone

2번 개발자는 1번 개발자의 저장소를 clone 합니다

```bash
git clone --mirror {1번 개발자 페어 프로그래밍 저장소 주소}
cd {1번개발자의저장소이름}
```

### 3. 복사한 저장소의 원격 저장소 설정

2번 개발자는 새롭게 생성한 원격 저장소를 복사해온 프로젝트의 원격 저장소로 설정합니다.

```bash
git remote set-url --push origin {2번 개발자의 새롭게 생성한 저장소 주소}
```

### 4. push

2번 개발자는 프로젝트를 Push 합니다.

```bash
git push --mirror
```