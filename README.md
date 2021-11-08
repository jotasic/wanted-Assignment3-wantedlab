# Assignment3-TW-JW-YY

원티드x위코드 백엔드 프리온보딩 과제3
- 과제 출제 기업 정보
  - 기업명 : 원티드랩

## Members
|이름   |github                   |담당 기능|
|-------|-------------------------|------------------|
|김태우 |[jotasic](https://github.com/jotasic)     | |
|고유영 |[lunayyko](https://github.com/lunayyko)   | |
|박지원 |[jiwon5304](https://github.com/jiwon5304) | |


## 과제 내용
> 다음과 같은 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 REST API 서버를 개발해주세요.

- 원티드 선호 기술스택
  - Python flask 또는 fastapi

### [데이터]
- 회사 정보
    - 회사 이름 (다국어 지원 가능)
- 회사 정보 예제
    - 회사 이름 (원티드랩 / Wantedlab)
- 데이터 셋은 원티드에서 제공
- 데이터셋 예제
  - 원티드랩 회사는 한국어, 영어 회사명을 가지고 있습니다. (모든 회사가 모든 언어의 회사명을 가지고 있지는 않습니다.)

|컬럼명 | company_name_ko   | company_name_en | company_name_ja |
|-------|-------------------|-----------------|-----------------|
|내용   | 원티드랩          | wantedlab       |                 |


### [REST API 기능]
- 회사명 자동완성
    - 회사명의 일부만 들어가도 검색이 되어야 합니다.
- 회사 이름으로 회사 검색
- 새로운 회사 추가

### [개발 조건]
- 제공되는 test case를 통과할 수 있도록 개발해야 합니다.
- ORM 사용해야 합니다.
- 결과는 JSON 형식이어야 합니다.
- database는 RDB를 사용해야 합니다.
- database table 갯수는 제한없습니다.
- 필요한 조건이 있다면 추가하셔도 좋습니다.
- Docker로 개발하면 가산점이 있습니다.


## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/PostgreSQL 14.0-0064a5?style=for-the-badge&logo=PostgreSQL&logoColor=white"/>&nbsp;
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/SWAGGER-5B8C04?style=for-the-badge&logo=Swagger&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 모델링
**추후 추가**


## API
**추후 추가**

## 구현 기능
**추후 추가**


## 배포정보
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 | http://18.188.189.173:8021/            |    |


## API TEST 방법
1. 우측 링크를 클릭해서 postman으로 들어갑니다. [링크](https://www.postman.com/wecode-21-1st-kaka0/workspace/assignment3/overview)

2. 정의된 SERVER_URL이 올바른지 확인 합니다. (18.188.189.173:8021)


3. 만약 Send버튼이 비활성화가 될 시 fork를 이용해서 해당 postman project를 복사해서 시도하길 바랍니다.
![image](https://user-images.githubusercontent.com/8219812/139912241-d6cb5831-23e8-4cbb-a747-f52c42601098.png)


## 설치 및 실행 방법
###  Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY
    cd Assignment3-TW-JW-YY
    ```
2. 가상 환경을 만들고 프로젝트에 사용한 python package를 받는다.
    ```bash
    conda create --name Assignment3-TW-JW-YY python=3.8
    conda actvate Assignment3-TW-JW-YY
    pip install -r requirements.txt
    ```

3. docker환경 설정 파일을 만든다.
      ```text
      # .dockerenv.dev_local
      
      DJANGO_SECRET_KEY='django시크릿키'
      ```

4. docker-compose를 통해서 db와 서버를 실행시킨다.
    ```bash
    docker-compose -f docker-compose-dev-local.yml up
    ```
    
5. 만약 백그라운드에서 실행하고 싶을 시 `-d` 옵션을 추가한다.
    ```bash
    docker-compose -f docker-compose-dev-local.yml up -d
    ```

###  배포용 
1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment3-TW-JW-YY
    cd Assignment3-TW-JW-YY
    ```

2. docker환경 설정 파일을 만든다.
  
3. 백엔드 서버용 .dockerenv.deploy_backend 파일을 만들어서 안에 다음과 같은 내용을 입력한다. manage.py와 같은 폴더에 생성한다.
      
    ```text
    # ..dockerenv.deploy_backend
    DJANGO_SECRET_KEY='django시크릿키'
    ```
   
4. DB 용 .dockerenv.deploy_db 파일을 만들어서 안에 다음과 같은 내용을 입력한다. manage.py와 같은 폴더에 생성한다.
  
    ```text
    # .dockerenv.deploy_db
    ```

5. docker-compose를 통해서 db와 서버를 실행시킨다.
    
    ```bash
    docker-compose -f docker-compose-deploy.yml up
    ```
    
6. 만약 백그라운드에서 실행하고 싶을 시 `-d` 옵션을 추가한다.
  
    ```bash
    docker-compose -f docker-compose-deploy.yml up -d
    ```

## 폴더 구조

```bash

```

## TIL정리 (Blog)
- 김태우 : 
- 고유영 :
- 박지원 : 

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
